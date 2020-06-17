import os
import re
import pandas
import datetime

#path to the log file
filePath="C:\\Users\\Administrator\\source\\repos\\Logfile\\logfile.log"

def logFile2dataFrame(filePath):
    """
    This function retrieves the log file, using a regular expression to finding the pattern of data
    Input: path to the log file
    Output: dataframe include three columns 'song, user, country'
    """
    dfLog = pandas.DataFrame( columns=[ 'song' , 'user' , 'country'] )
    # Regex used to match relevant data
    line_regex = re.compile(r"(?<=\|)[^|]*(?=\|)")
    
    with open(filePath, "r") as in_file:
        numRows=-1
    # loop over each log line
        for line in in_file:
            # if log line matches the regex, split | and add to dataframe
            if (line_regex.search(line)):
                tokens=line.split("|")
                sng=tokens[0]
                user=tokens[1]
                country=tokens[2].strip()
                numRows +=1
                dfLog.loc[numRows]=[sng,user,country]
            #else:
            #    dfLog.loc[numRows,'Message'] += line
    return dfLog

df=logFile2dataFrame(filePath)

##MUST HAVE COUNTRY TOP 50 

df_groupby=df.groupby(['country','song']).agg({'user':'count'})
df_rank = df_groupby['user'].groupby(level=0, group_keys=False)
df_rank=df_rank.apply(lambda x: x.sort_values(ascending=False)).to_frame().reset_index()
#Combine column song and user of the data frame to get required format
df_rank['song_count']= df_rank["song"] +":"+ df_rank["user"].astype(str)
df_output =df_rank.groupby(['country'])['song_count'].apply(lambda x: ", ".join(x.astype(str))).reset_index()

#export dataframe to txt file
filename_country='country_top50_'+str(datetime.date.today())
df_output.to_csv(f'{filename_country}.txt', sep='|', header=False, index=False )


##NICE TO HAVE USER TOP 50

dfgUser=df.groupby(['user','song'])['user'].count().sort_values(ascending=False).reset_index(name='n_users')
#Combine column song and user of the data frame to get required format
dfgUser['song_count']= dfgUser["song"] +":"+ dfgUser["n_users"].astype(str)
dfg_user_output =dfgUser.groupby(['user'])['song_count'].apply(lambda x: ", ".join(x.astype(str))).reset_index()

#export dataframe to txt file
filename_user='user_top50_'+str(datetime.date.today())
dfg_user_output.to_csv(f'{filename_user}.txt', sep='|', header=False, index=False )

