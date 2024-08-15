# ''' Testing schedulingalgo.py'''
# from schedulingalgo import *

# schedule_ex1 = pd.DataFrame({
#     'Job ID': [1,2,3,4,5,6,7,8],
#     'Processing Time':[5,9,2,6,7,8,5,7],
#     'Time to deadline':[8,12,13,15,18,26,26,30]
# })

# print('Our original data set is:\n')
# print(schedule_ex1.to_string(index=False))

# # ORDERING JOBS BASED OFF OF EARLIEST DUE DATE
# EDD_schedule_ex1 = EDDAlgorithm(schedule_ex1)
# print(EDD_schedule_ex1.to_string(index=False))

# # TO USE MOORE, FIRST FIND FIRST LATE JOB IN EDD SCHEDULE
# [first_late,longest_deadline] = findJobIDToDiscard(EDD_schedule_ex1)
# print(f"The first late job is {first_late}.")
# print(f"Up to the first late job, the longest job is {longest_deadline}.")

# # NEXT, RUN MOORES ALGO
# Moores_schedule_ex1 = MooresAlgorithm(schedule_ex1, printTable = False)
# print('The final schedule according to Moores algorithm is:\n')
# print(Moores_schedule_ex1.to_string(index=False))

# # WE CAN COUNT THE NUMBER OF LATE JOBS
# number_late = countLateJobs(Moores_schedule_ex1)
# print(f'There are {number_late} late jobs.')

''' Testing moores-hodgson binding'''
import moores-hodgson
