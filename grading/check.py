import utils
import resource
import subprocess
from pycparser import c_ast


# 195 MiB of memory
BYTES = 195 * 1024 * 1024


# C loop visitor
class LoopCondVisitor(c_ast.NodeVisitor):

    def __init__(self):
        self.found = False

    def visit_While(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_DoWhile(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_Goto(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_If(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_Switch(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_TernaryOp(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_For(self, node):
        self.found = True
        self.generic_visit(node)

    def reset(self):
        self.found = False


# C free call visitor
class FreeCall(c_ast.NodeVisitor):

    def __init__(self):
        self.count = 0

    def visit_FuncCall(self, node):
        if node.name.name.lower() == 'free':
            self.count += 1
        self.generic_visit(node)

    def reset(self):
        self.count = 0


class ReallocCall(c_ast.NodeVisitor):

    def __init__(self):
        self.count = 0

    def visit_FuncCall(self, node):
        if node.name.name.lower() == 'realloc':
            self.count += 1
        self.generic_visit(node)

    def reset(self):
        self.count = 0


# checks vector
def check_ex1():
    try:
        grade = 0

        # compile
        task = utils.make(target='vector')
        if task.returncode != 0:
            return (round(grade), utils.failed('compilation error'), task.stderr.decode().strip())
        
        # check for free calls
        v = FreeCall()
        ast = utils.parse_c('ex1/vector')
        
        # vector_new
        v.reset()
        v.visit(utils.find_func(ast, 'vector_new'))
        if v.count == 0:
            return (round(grade), utils.failed('[vector_new] don\'t forget to call free... ¯\\_(⊙︿⊙)_/¯'), '')
        else:
            grade += 8
        
        # vector_delete
        v.reset()
        v.visit(utils.find_func(ast, 'vector_delete'))
        if v.count < 2:
            return (round(grade), utils.failed('[vector_delete] don\'t forget to call free... ¯\\_(⊙︿⊙)_/¯'), '')
        else:
            grade += 8
        
        # vector_set
        r = ReallocCall()
        v.reset()
        r.reset()
        v.visit(utils.find_func(ast, 'vector_set'))
        r.visit(utils.find_func(ast, 'vector_set'))
        if v.count == 0 and r.count == 0:
            return (round(grade), utils.failed('[vector_set] don\'t forget to call free or use realloc... ¯\\_(⊙︿⊙)_/¯'), '')
        else:
            grade += 9
        
        # run tests
        task = utils.execute(cmd=['./vector'], timeout=5)
        if task.returncode != 0:
            return (round(grade), utils.failed('runtime error'), task.stderr.decode().strip())
        
        # Output
        output = task.stdout.decode().strip().split('\n')
        f = open('ex1.expected', 'r')
        expected = f.read().strip().split('\n')
        f.close()

        wrong = 0
        for (exp, out) in zip(expected, output):
            exp = exp.strip()
            out = out.strip()
            if exp == out:
                grade += 75 / 17
            else:
                wrong += 1
        
        # grade
        if wrong == 17:
            return (round(grade), utils.failed('all tests failed'), '')
        elif wrong != 0:
            return (round(grade), utils.incomplete('some tests failed...'), '')
        else:
            return (100, utils.passed(), '')
    except subprocess.TimeoutExpired:
        return (round(grade), utils.failed('TIMEOUT'), '')
    except Exception as e:
        print(e)
        return (0, utils.failed('memory limit exceeded'), '')


def lab3_struct():
    not_found = utils.expected_files([ './ex1/vector.c' ])
    if len(not_found) == 0:
        table = []
        
        ex1_result = check_ex1()
        table.append(('1. vector', *ex1_result[0: 2]))
        errors = ''
        errors += utils.create_error('vector', ex1_result[2])
        errors = errors.strip()
        grade = 0
        grade += ex1_result[0]
        grade = round(grade)
        grade = min(grade, 100)
        report = utils.report(table)
        print(report)
        if errors != '':
            report += '\n\nMore Info:\n\n' + errors
        return utils.write_result(grade, report)
    else:
        utils.write_result(0, 'missing files: %s' % (','.join(not_found)))


if __name__ == '__main__':
    resource.setrlimit(resource.RLIMIT_AS, (BYTES, BYTES))
    lab3_struct()
    utils.fix_ownership()
