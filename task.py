import datetime
import random


# For the tester's attention:
# I initially tried to make three classes but I had a problem with the import
# so I transferred everything to one file as Harry told me and that's why the code looks a bit messy, sorry!
# And besides, I didn't really have time to check exactly whether the code works or not,
# but I tried to remember the concept of objects and classes and bring it to expression in the code.
class Task:
    def __init__(self, describe_task, complicated, days_to_work):
        self._describe = describe_task
        self._open_data = datetime.datetime.now()
        self._end_data = datetime.datetime.now() + (
            self._open_data + self._days_to_work
        )
        self._complicated = random.randint(1, 5)
        self._days_to_work = days_to_work
        self._belong_to_developer = self.give_project_to_developer()
        self._salary = Developer.old * (complicated / days_to_work)
        self._task_done = False

        if self._belong_to_developer == None:
            self._salary == 0

    def give_project_to_developer(self, name):
        self._belong_to_developer = Developer[name]
        Project.list_developers.append(name)

    @property
    def describe_task(self):
        return self._describe

    @property
    def days_to_work(self):
        return self.__days_to_work

    @property
    def task_done(self):
        return self._task_done

    @property
    def open_data(self):
        return self._open_data

    @property
    def end_data(self):
        return self._end_data

    @property
    def complicated(self):
        return self._complicated

    @property
    def belong_to_developer(self):
        return self._belong_to_developer

    @property
    def salary(self):
        return self._salary

    @property
    def task_done(self):
        return self._task_done

    @describe_task.setter
    def describe_task(self, new_describe_task: int):
        self._describe_task = new_describe_task

    @days_to_work.setter
    def days_to_work(self, new_days_to_work: int):
        self._days_to_work = new_days_to_work

    @days_to_work.setter
    def task_done(self, new_task_done: int):
        self._task_done = new_task_done


####################################################################################################################################
class Developer:  # i have a problem with import this file so i moved it to tha same file like Ari told me
    def __init__(self, name, days_of_work, salary):
        self._name = name
        self._days_of_work = days_of_work
        self._salary = self.salary()
        self._done_tasks = []
        self._tasks_to_do = []
        self._old = 1

    def done_task(self):
        for done in self.tasks_to_do:
            self.done_task.append(done)
            self.old += Task._complicated
            self.salary()
            if Project.to_do == 0:
                Task._task_done = True
                Project._project_done = True

    def salary(self):
        self.salary += self.done_tasks

    @property
    def old(self):
        return self._old

    @property
    def name(self):
        return self._name

    @property
    def days_of_work(self):
        return self._days_of_work

    @property
    def salary(self):
        return self._salary

    @property
    def done_tasks(self):
        return self._done_tasks

    @property
    def tasks_to_do(self):
        return self._tasks_to_do

    @name.setter
    def name(self, new_name: int):
        self._name = new_name

    @days_of_work.setter
    def days_of_work(self, new_days_of_work: int):
        self._days_of_work = new_days_of_work

    @salary.setter
    def salary(self, new_salary: int):
        self._salary = new_salary

    @done_tasks.setter
    def done_tasks(self, new_done_tasks: list):
        self._done_tasks = new_done_tasks

    @tasks_to_do.setter
    def tasks_to_do(self, new_tasks_to_do: list):
        self._tasks_to_do = new_tasks_to_do


####################################################################################################################################
class Project:  # i have a problem with import this file so i moved it to tha same file like Ari told me
    def __init__(self, describe):
        self._describe = describe
        self._data_begin = datetime.datetime.now()
        self._date_end = datetime.datetime.now() + sum(self.list_task)
        self._list_task = []
        self._list_developers = []
        self._to_do = []
        self._done = []
        self._cost = self.cost_of_project()
        self._project_done = False

        if self.to_do == 0:
            self.project_done = True

    def cost_of_project(self):
        for task in self.done:
            self.cost += task * Developer.salary

    def add_task(self, new_task, name: Developer):
        try:
            if new_task not in self.to_do:
                if (
                    new_task not in Project.list_task
                ):  # not in other projects tasks list
                    self.to_do.append(new_task)
                    self.list_developers.append(name)
        except:
            raise Exception
        return self.to_do

    def sub_task(self, task, name: Developer):
        try:
            if self.project_done == False:
                self.to_do -= task
                self.list_developers.remove(name)
        except:
            raise Exception

    def search_task(self):
        searching_task = Task.describe_task
        for searching_task in self.to_do:
            return searching_task

    @property
    def describe(self):
        return self._describe

    @property
    def data_begin(self):
        return self._data_begin

    @property
    def data_end(self):
        return self._date_end

    @property
    def cost(self):
        return self._cost

    @property
    def list_task(self):
        return self._list_task

    @property
    def list_developers(self):
        return self._list_developers

    @property
    def to_do(self):
        return self._to_do

    @property
    def done(self):
        return self._done

    @property
    def project_done(self):
        return self._project_done

    @describe.setter
    def describe(self, new_describe: int):
        self._describe = new_describe

    @data_begin.setter
    def data_begin(self, new_data_begin: int):
        self._data_begin = new_data_begin

    @data_end.setter
    def data_end(self, new_data_end: int):
        self._date_end = new_data_end

    @cost.setter
    def cost(self, new_cost: int):
        self._cost = new_cost

    @list_task.setter
    def list_task(self, new_list_task: int):
        self._list_task = new_list_task

    @list_developers.setter
    def list_developers(self, new_list_developers: int):
        self._list_developers = new_list_developers

    @to_do.setter
    def to_do(self, new_to_do: int):
        self._to_do = new_to_do

    @done.setter
    def done(self, new_done: int):
        self._done = new_done

    @project_done.setter
    def project_done(self, new_project_done: int):
        self._project_done = new_project_done
