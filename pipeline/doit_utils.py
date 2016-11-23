#! /usr/bin/env python
from doit.cmd_base import TaskLoader
from doit.doit_cmd import DoitMain
from doit.task import dict_to_task

class TaskFailed(Exception):
    pass


_task_count = 1
def make_task(task_dict_func):
    '''Wrapper to decorate functions returning pydoit
    `Task` dictionaries and have them return pydoit `Task`
    objects
    '''
    def d_to_t(*args, **kwargs):
        global _task_count
        ret_dict = task_dict_func(*args, **kwargs)
        if 'name' not in ret_dict:
            name = "{0}.func<{1}>".format(str(_task_count), task_dict_func.__name__)
            _task_count += 1

            ret_dict['name'] = name
        return dict_to_task(ret_dict)
    return d_to_t


def run_tasks(tasks, args, config={'verbosity': 0}):
    '''Given a list of `Task` objects, a list of arguments,
    and a config dictionary, execute the tasks.
    '''

    if type(tasks) is not list:
        raise TypeError('tasks must be of type list.')

    class Loader(TaskLoader):
        @staticmethod
        def load_tasks(cmd, opt_values, pos_args):
            return tasks, config

    status = DoitMain(Loader()).run(args)
    if status:
        raise TaskFailed(status)
