#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day7_05_apscheduler.py
@time: 2022/10/10  15:06
# @describe: Python 定时任务框架 apscheduler

1. github 地址：https://github.com/agronholm/apscheduler
    博客园大佬的文章：https://www.cnblogs.com/csnd/p/16464695.html

2. apscheduler 基本概念介绍：
    说到定时任务，会想起 linux 自带的 crontab ，windows 自带的任务计划，都可以实现守时任务。操作系统基本都会提供定时任务的实现，
    但是如果想要更加精细化的控制，或者说任务程序需要跨平台运行，最好还是自己实现定时任务框架，Python中定时任务的解决方案，总体来说有四种，
    分别是： crontab、 scheduler、 Celery、 APScheduler，其中 crontab 不适合多台服务器的配置、 scheduler 太过于简单、
    Celery 依赖的软件比较多，比较耗资源。最好的解决方案就是 APScheduler。Python 的 apscheduler 提供了非常丰富而且方便易用的定时任务接口。

    apscheduler ( advance python scheduler ) 是 Python 中的任务调度库，使用起来十分方便 。
    提供了基于 日期、固定时间间隔、crontab 类型的任务，可以在主程序的运行过程中快速增加新作业或删除旧作业，如果把作业存储在数据库中，
    那么作业的状态会被保存，当调度器重启时，不必重新添加作业，作业会恢复原状态继续执行。apscheduler 可以当作一个跨平台的调度工具来使用，
    可以做为 linux 系统 crontab 工具或 windows 计划任务程序的替换。注意，apscheduler 不是一个守护进程或服务，
    它自身不带有任何命令行工具。它主要是要在现有的应用程序中运行，也就是说，apscheduler 为我们提供了构建专用调度器或调度服务的基础模块

3.安装：pip install apschedule

4. APScheduler 组件介绍
    APScheduler 由5个部分组成：触发器、调度器、任务存储器、执行器、任务事件。

    任务 job：任务id 和 任务执行 func
    触发器（triggers）：确定任务何时开始执行。触发器包含调度逻辑，描述一个任务何时被触发，按日期或按时间间隔或按 cronjob 表达式三种方式触发。每个作业都有它自己的触发器，除了初始配置之外，触发器是完全无状态的。
    作业存储器（job stores）： 也叫 "任务存储器"，保存任务的状态。作业存储器指定了作业被存放的位置，默认情况下作业保存在内存，也可将作业保存在各种数据库中，当作业被存放在数据库中时，它会被序列化，当被重新加载时会反序列化。作业存储器充当保存、加载、更新和查找作业的中间商。在调度器之间不能共享作业存储。
    执行器（executors）：确定任务怎么执行。执行器是将指定的作业（调用函数）提交到线程池或进程池中运行，当任务完成时，执行器通知调度器触发相应的事件。
    调度器（schedulers）：任务调度器，属于控制角色，通过它配置作业存储器、执行器和触发器，添加、修改和删除任务。调度器协调触发器、作业存储器、执行器的运行，通常只有一个调度程序运行在应用程序中，开发人员通常不需要直接处理作业存储器、执行器或触发器，配置作业存储器和执行器是通过调度器来完成的，调度器会自动完成。调度器串联任务的整个生命周期，添加编辑任务到任务存储器,在任务的执行时间到来时，把任务交给执行器执行返回结果；同时发出事件监听，监控任务事件 。
    任务事件 event：监控任务执行异常情况

"""
import time
from datetime import datetime
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler


def job(text):
    print(text)


scheduler = BlockingScheduler(timzone='Asia/Shanghai')

""" 触发器参数：date 定时，作业只执行一次。 """
# 在 2022-10-10 00:00:00 运行一次job 方法
scheduler.add_job(job, 'date', run_date=date(2022, 10, 10), args=['text1'])

# 在 2022-10-10 15:55:00 运行一次job 方法
scheduler.add_job(job, 'date', run_date=datetime(2022, 10, 10, 15, 56, 0), args=['text2'])

# 在 2022-10-10 16:02:01 运行一次job 方法
scheduler.add_job(job, 'date', run_date='2022-10-10 16:31:01', args=['text3'])
# 启动调度器
# scheduler.start()




""" 
触发器参数：interval 间隔调度
    weeks (int) – 等待的周数
    days (int) – 等待的天数
    hours (int) – 等待的小时
    minutes (int) – 等待的分钟
    seconds (int) – 等待的秒
    start_date (datetime|str) – 间隔计算的起点
    end_date (datetime|str) – 触发的最新可能日期/时间
    timezone (datetime.tzinfo|str) – 用于日期/时间计算的时区
"""


def job1(text):
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(f'{text} --- {t}')


scheduler1 = BlockingScheduler()
# 每个一分钟，运行一次 job 方法
scheduler1.add_job(job1, 'interval', minutes=1, args=['job1'])
# 在 2022-10-10 16:20:00至 2022-10-10 16:30:00 期间，每隔1分30秒 运行一次 job 方法
scheduler1.add_job(job1, 'interval', minutes=1, seconds=30, start_date='2022-10-10 16:20:00',
                   end_date='2022-10-10 16:30:00', args=['job2'])
# 启动调度器
# scheduler1.start()



""" 
cron 调度：
    year (int|str) – 4位数年份
    month (int|str) – 月（1-12）
    day (int|str) – 日期 (1-31)
    week (int|str) – ISO周 (1-53)
    day_of_week (int|str) – 工作日的编号或名称（0-6或周一、周二、周三、周四、周五、周六、周日）
    hour (int|str) – 小时 (0-23)
    minute (int|str) – 分钟 (0-59)
    second (int|str) – 秒 (0-59)
    start_date (datetime|str) – 触发的最早日期/时间（含）
    end_date (datetime|str) – 触发的最新可能日期/时间（包括）
    timezone (datetime.tzinfo|str) – 用于日期/时间计算的时区（默认为调度程序时区）
 """
# 6-8,11-12月第三个周五 00:00, 01:00, 02:00, 03:00运行
scheduler1.add_job(job1, 'cron', month='6-8, 11-12', day='3rd fri', hour='0-3', args=['job1'])

# 每周一到周五运行 直到2024-05-30 00:00:00
scheduler1.add_job(job1, 'cron', day_of_week='mon-fri', hour=5, minute=30, end_date='2024-05-30', args=['job1'])


# 也可以用表达式类型，可以用以下方式：
def job2(text):
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(f'{text} -- {t}')


scheduler2 = BlockingScheduler()
# 在每天22点，每隔1分钟，运行一次 job2 方法
scheduler2.add_job(job2, 'cron', hour=22, minute='*/1', args=['job1'])
# 在每天22 和23点 的25分，运行一次 job2 方法
scheduler2.add_job(job2, 'cron', hour='22-23', minute='25', args=['job2'])
# 在每天8点，运行一次 job2 方法
scheduler2.add_job(job2, 'cron', hour='8', args=['job2'])
# 在每天 8点、 20点，各运行一次 job2 方法，设置最大运行实例数
scheduler2.add_job(job2, 'cron', hour='8, 20', minute=30, max_instances=4, args=['job3'])
scheduler2.start()




""" 
任务存储器：
    任务存储器决定任务的保存方式， 默认存储在内存中（MemoryJobStore），重启后就没有了。
    不同的任务存储器可以在调度器的配置中进行配置（见调度器）。APScheduler 支持的任务存储器有：
    
         apscheduler.jobstores.memory：内存
         apscheduler.jobstores.mongodb：存储在 mongodb
         apscheduler.jobstores.redis：存储在 redis
         apscheduler.jobstores.rethinkdb：存储在 rethinkdb
         apscheduler.jobstores.sqlalchemy：支持 sqlalchemy 的数据库如 mysql，sqlite 等
         apscheduler.jobstores.zookeeper：zookeeper

"""



"""
执行器：
    执行器决定如何执行任务；常用的有 pool(线程/进程) 和 gevent(io多路复用，支持高并发)，默认为 pool 中线程池， 
    不同的执行器可以在调度器的配置中进行配置（见调度器）。执行器的选择取决于应用场景。
    通常默认的 ThreadPoolExecutor 已经在大部分情况下是可以满足我们需求的。如果我们的任务涉及到一些 CPU密集计算的操作。
    那么应该考虑 ProcessPoolExecutor。然后针对每种程序， apscheduler也设置了不同的 executor：

         apscheduler.executors.asyncio：同步 io，阻塞
         apscheduler.executors.gevent：io 多路复用，非阻塞
         apscheduler.executors.pool:  线程ThreadPoolExecutor 和 进程ProcessPoolExecutor
         apscheduler.executors.twisted：基于事件驱动

"""



"""
调度器：
   调度器的主循环其实就是反复检查是不是有到时需要执行的任务，分以下 2 步进行：

        1.询问自己的每一个作业存储器，有没有到期需要执行的任务，如果有，计算这些作业中每个作业需要运行的时间点如果时间点有多个，做 coalesce 检查。
            设置 coalesce 为 False ：设置这个目的是，比如由于某个原因导致某个任务积攒了很多次没有执行（比如有一个任务是1分钟跑一次，
            但是系统原因断了5分钟），如果 coalesce = True ，那么下次恢复运行的时候，会只执行一次，而如果设置 coalesce = False ，
            那么就不会合并，会5次全部执行。
        2.提交给执行器按时间点运行。 
    
    在配置调度器前，首先要选取合适应用环境场景的 调度器，存储器 和 执行器。APScheduler 支持的调度器方式如下，
    比较常用的为 BlockingScheduler 和 BackgroundScheduler，下面是各调度器的适用场景，可以满足绝大多数的应用环境：

        BlockingScheduler：适用于调度程序是进程中唯一运行的进程，调用start函数会阻塞当前线程，不能立即返回。
        BackgroundScheduler：适用于调度程序在应用程序的后台运行，调用 start 后主线程不会阻塞。
        AsyncIOScheduler：适用于使用了 asyncio 模块的应用程序。
        GeventScheduler：适用于使用 gevent 模块的应用程序。
        TwistedScheduler：适用于构建 Twisted 的应用程序。
        QtScheduler：适用于构建 Qt 的应用程序。
        
    调度器可以操作任务（并为任务指定触发器、任务存储器和执行器）和监控任务。

"""



"""
作业存储器的选择有两种：
    一 是内存，也是默认的配置。适用场景：重启整个应用程序后，作业会被重新添加到调度器中，此时简单的选取内存作为作业存储器即简单又高效。
    二 是 数据库。适用场景：当调度器重启或应用程序崩溃时需要作业从中断位置恢复正常运行，那么可以选择将作业存储在数据库中，至于适用什么数据库，
        可以自由选择，PostgreSQL 是推荐的选择，因为它具有强大的数据完整性保护。

"""



"""
执行器的选择取决于应用场景：
    通常默认的 ThreadPoolExecutor 已经足够好。
    如果作业负载涉及CPU 密集型操作，那么应该考虑使用 ProcessPoolExecutor，甚至可以同时使用这两种执行器，
        将 ProcessPoolExecutor 行器添加为二级执行器。
"""


"""
调度器 的 配置：
    调度器配置：在 add_job 我们看到 jobstore 和 executor 都是 default，APScheduler 在定义调度器时可以指定不同的任务存储和执行器，
        以及初始的参数   
"""


"""
启动 调度器：
    启动调度器前需要先添加作业，有两种方法向调度器添加作业：
    
        一是通过接口 add_job()，
        二是通过使用 函数装饰器，其中 add_job() 返回一个 apscheduler.job.Job 类 的实例，用于后续修改或删除作业。

"""