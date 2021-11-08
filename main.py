from data_processing import Find_Metrics, Query, try_connect

if __name__ == '__main__':
    if try_connect() == 'JOB DONE':
        print('NICE')
        