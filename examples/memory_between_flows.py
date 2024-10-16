import controlflow as cf

thread_id = "test-thread"


@cf.flow(thread=thread_id)
def flow_1():
    task = cf.Task("get the user's name", result_type=str, interactive=True)
    return task.run()


@cf.flow(thread=thread_id)
def flow_2():
    task = cf.Task("write the user's name backwards, if you don't know it, say so")
    return task.run()


if __name__ == "__main__":
    flow_1()
    flow_2()
