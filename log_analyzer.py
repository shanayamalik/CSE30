#===== You may add import statements below this line ----->
import json
import pandas
from typing import List
import re # regular expression library
#===== <----- Please keep import statements above this line

def log_to_dataframe(src_log_filepath: str) -> pandas.DataFrame:
    '''
    - Parameters:
        - src_log_filepath: path to the log file
    - Returns:
        - pandas.DataFrame: a pandas.DataFrame object parsed from
          the log file
    '''
    #===== Please enter your implementation below this line ----->
    hosts = [] #appending to lists instead of a dataframe made it faster
    tss = []; methods = []; urls = []; versions = []; rcs = []; css = []

    # https://docs.python.org/3/library/re.html and https://docs.python.org/3/howto/regex.html
    rx = re.compile('^\s*(?P<host>\S+?) \S+ \S+ \[(?P<timestamp>.+?)\]' +
                    ' "(?P<method>\S+?) (?P<url>.+?) (?P<version>\S+?)"' +
                    ' (?P<response_code>\S+?) (?P<content_size>\S+?)\s*$')
    # (?P<name>...?) is a name-d group available from matching

    with open(src_log_filepath, 'r') as f:
      for line in f:
        m = rx.match(line)
        if m.lastindex == 7: # only collect data if all 7 groups matched

          hosts.append(m.group('host'))

          # https://stackoverflow.com/questions/3411771
          tss.append(pandas.Timestamp(m.group('timestamp').replace(':', ' ', 1),
                                      tz='UTC')) # convert to UTC

          methods.append(m.group('method'))
          urls.append(m.group('url'))
          versions.append(m.group('version'))

          rc = m.group('response_code')
          if rc.isdigit():
            rcs.append(int(rc))
          else:
            rcs.append(pandas.NA) # integer NANs https://stackoverflow.com/a/67270477

          cs = m.group('content_size')
          if cs.isdigit():
            css.append(int(cs))
          else:
            css.append(pandas.NA)

    return pandas.DataFrame({'host': hosts, 'timestamp': tss, 'method': methods,
                             'url': urls, 'version': versions,
                             'response_code': rcs, 'content_size': css})
    #===== <----- Please keep your implementation above this line
    pass

def get_num_of_distinct_resp_code(data: pandas.DataFrame) -> int:
    '''
    - Parameters:
        - data: input dataframe, read from your CSV file
    - Returns:
        - int: number of distinct response code
    '''
    #===== Please enter your implementation below this line ----->
    return data['response_code'].nunique(dropna=True)
    #===== <----- Please keep your implementation above this line
    pass

def get_median_content_size(data: pandas.DataFrame) -> int:
    '''
    - Parameters:
        - data: input dataframe, read from your CSV file
    - Returns:
        - int: median content size
    '''
    #===== Please enter your implementation below this line ----->
    return int(data['content_size'].median(skipna=True))
    #===== <----- Please keep your implementation above this line
    pass

def get_most_freq_hosts(data: pandas.DataFrame, numOfHosts: int) -> List[str]:
    '''
    - Parameters:
        - data: input dataframe, read from your CSV file
        - numOfHosts: top `numOfHosts` most frequency hosts
    - Returns:
        - List[str]: list of strings containing top `numOfHosts` most
          frequent hosts; ordered from top 1 to top `numOfHosts`
    '''
    #===== Please enter your implementation below this line ----->
    return data['host'].value_counts()[:numOfHosts].index.tolist() # .index gets the names
    #===== <----- Please keep your implementation above this line
    pass

def get_most_freq_urls(data: pandas.DataFrame, numOfUrls: int) -> List[str]:
    '''
    - Parameters:
        - data: input dataframe, read from your CSV file
        - numOfUrls: top `numOfUrls` most frequency URLs
    - Returns:
        - List[str]: list of strings containing top `numOfUrls`
          most frequent URLs; ordered from top 1 to top
          `numOfUrls`
    '''
    #===== Please enter your implementation below this line ----->
    return data['url'].value_counts()[:numOfUrls].index.tolist()
    #===== <----- Please keep your implementation above this line
    pass

def get_top_urls_recv_err(data: pandas.DataFrame, numOfUrls: int) -> List[str]:
    '''
    - Parameters:
        - data: input dataframe, read from your CSV file
        - numOfUrls: top `numOfUrls` URLs that received error
          response codes
    - Returns:
        - List[str]: list of strings containing top `numOfUrls`
          URLs that received error response codes; ordered from
          top 1 to top `numOfUrls`
    '''
    #===== Please enter your implementation below this line ----->
    return data[data['response_code'] != 200]['url'].value_counts( # not 200 from assignment
        )[:numOfUrls].index.tolist()
    #===== <----- Please keep your implementation above this line
    pass

def get_num_of_req_recv_404(data: pandas.DataFrame) -> int:
    '''
    - Parameters:
        - data: input dataframe, read from your CSV file
    - Returns:
        - int: number of requests with a 404 response code
    '''
    #===== Please enter your implementation below this line ----->
    return len(data[data['response_code'] == 404])
    #===== <----- Please keep your implementation above this line
    pass

def get_num_of_unique_hosts_daily(data: pandas.DataFrame) -> List[int]:
    '''
    - Parameters:
        - data: input dataframe, read from your CSV file
    - Returns:
        - List[int]: List of integers of unique hosts on each
          day, ordered from the earliest to latest date
    '''
    #===== Please enter your implementation below this line ----->
    # https://stackoverflow.com/questions/54564340/
    return data.groupby([data['timestamp'].dt.date])['host'].nunique().tolist()
    #===== <----- Please keep your implementation above thisdropn
    pass

def get_avg_num_of_req_per_host_daily(data: pandas.DataFrame) -> List[int]:
    '''
    - Parameters:
        - data: input dataframe, read from your CSV file
    - Returns:
        - List[int]: List of integers of average requests per
        host on each day, ordered from the earliest to latest
        date
    '''
    #===== Please enter your implementation below this line ----->
    # https://stackoverflow.com/questions/37571870/ and https://www.w3schools.com/python/pandas/ref_df_agg.asp
    return data.groupby([data['timestamp'].dt.date])['host'].agg(
        lambda x: x.count() // x.nunique()).tolist() # integer division rounds the value down
    #===== <----- Please keep your implementation above this line
    pass

def write_results_to_json(res1: int, res2: int, res3: List[str],
                          res4: List[str], res5: List[str], res6: int,
                          res7: List[int], res8: List[int],
                          dest_json_path: str) -> None:
    '''
    - Parameters:
        - res1: result generated by the function corresponding to question 1
        - res2: result generated by the function corresponding to question 2
        - res3: result generated by the function corresponding to question 3
        - res4: result generated by the function corresponding to question 4
        - res5: result generated by the function corresponding to question 5
        - res6: result generated by the function corresponding to question 6
        - res7: result generated by the function corresponding to question 7
        - res8: result generated by the function corresponding to question 8
        - dest_json_path: filepath to write the json file to
    '''
    #===== Please enter your implementation below this line ----->
    d = {'get_num_of_distinct_resp_code': res1,
         'get_median_content_size': res2,
         'get_most_freq_hosts': res3,
         'get_most_freq_urls': res4,
         'get_top_urls_recv_err': res5,
         'get_num_of_req_recv_404': res6,
         'get_num_of_unique_hosts_daily': res7,
         'get_avg_num_of_req_per_host_daily': res8}
    with open(dest_json_path, 'w') as f:
      json.dump(d, f, indent=4, sort_keys=False)
    #===== <----- Please keep your implementation above this line
    pass
