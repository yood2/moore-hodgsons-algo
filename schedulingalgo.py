#Install the necessary packages
import pandas as pd


########################################
#Define Update Times Algorithm to compute Order in schedule, completion time, and whether late
#Input: Data frame with (at least) columns 'Time to deadline' and 'Processing Time'
########################################
def UpdateTimes(schedule):

    schedule['Order in schedule'] = [(i+1) for i in range(0,len(schedule.index))]
    schedule['Completion Time'] = [sum(schedule['Processing Time'][0:(i+1)]) for i in range (0, len(schedule.index))]
    schedule['Late?'] = [schedule['Completion Time'].iloc[i]>schedule['Time to deadline'].iloc[i] for i in range(0,len(schedule.index))]

    return schedule

########################################
#Define Earliest Due Date (EDD) Algorithm
#Input: Data frame with columns 'Time to deadline' and 'Processing Time'
########################################
def EDDAlgorithm(df_original):

    df_EDD = df_original.sort_values(by=['Time to deadline'])
    df_EDD = UpdateTimes(df_EDD)

    return df_EDD


########################################
#Define Method for Identifying First Late
#and longest time
#Input: Data frame with columns 'Time to deadline', 'Processing Time',
#       'Order in schedule', 'Completion Time', 'Late?'
#Output: Job indices
########################################
def findJobToDiscard(df):

    if True not in set(df['Late?']):
        print('All jobs are on time, so there is nothing to discard.')
        return

    else:

        first_late = (df['Late?'] == 1).argmax()   #Find first late
        df_first_late = df.iloc[:(first_late+1)]   #Look at all jobs up to first late
        longest_deadline = df_first_late['Processing Time'].idxmax()   #Among all jobs up to first late, find one with longest flow time and discard

    return [first_late,longest_deadline]


########################################
#Define method that just prints job IDs corresponding to findJobToDiscard.
#This is only for show, no functional purpose.
#Input: Data frame with columns 'Time to deadline', 'Processing Time',
#       'Order in schedule', 'Completion Time', 'Late?'
#Output: Job Ids
########################################
def findJobIDToDiscard(df):

    if True not in set(df['Late?']):
        print('All jobs are on time, so there is nothing to discard.')
        return

    else:

        first_late = (df['Late?'] == 1).argmax()   #Find first late
        df_first_late = df.iloc[:(first_late+1)]   #Look at all jobs up to first late
        longest_deadline = df_first_late['Processing Time'].idxmax()   #Among all jobs up to first late, find one with longest flow time and discard
    return [df['Job ID'].iloc[first_late],df['Job ID'][longest_deadline]]

########################################
#Define method to count number of late.
#This is only for show, no functional purpose.
#Input: Data frame with columns 'Time to deadline', 'Processing Time',
#       'Order in schedule', 'Completion Time', 'Late?'
#Output: Number of late jobs.
########################################
def countLateJobs(df):

    if True not in set(df['Late?']):
        return 0

    else:
        return df['Late?'].value_counts()[True]


########################################
#Define Moore's Algorithm
########################################
def MooresAlgorithm(original_schedule, printTable = False):

    current_schedule = EDDAlgorithm(original_schedule)

    if(printTable):
        print('The first EDD Schedule is:\n')
        print(current_schedule.to_string(index=False))


    #We start with an empty discard pile
    discarded_jobs = []

    #Now we start the repetition
    while(True in set(current_schedule['Late?'])):

        [first_late, longest_deadline] = findJobToDiscard(current_schedule) #Find job to discard

        if(printTable):
            print('The first late job is job', current_schedule['Job ID'].iloc[first_late])
            print('Up to the first late job, the job with the longest processing time is job', current_schedule['Job ID'][longest_deadline], 'so, we discard this job.\n')

        discarded_jobs.append(longest_deadline)                    #Add the long job to the discard pile
        current_schedule = current_schedule.drop(longest_deadline) #Remove the discarded jobs from our schedule (at least for now)
        current_schedule = EDDAlgorithm(current_schedule)          #Find the new EDD

        #Uncomment to print
        if(printTable):
            print(f'The new EDD (without discarded jobs) is:\n')
            print(current_schedule.to_string(index=False))
            print('\n')

    #---------   END WHILE LOOP

    current_schedule = pd.concat([current_schedule,original_schedule.iloc[discarded_jobs]], sort = False) #Add back discarded jobs
    current_schedule = UpdateTimes(current_schedule) #Compute the final order, completion times, and lateness

    return current_schedule
