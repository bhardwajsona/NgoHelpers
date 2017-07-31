
                                                      ##### NIDHI'S CODE  #####

from twython import Twython, TwythonError,TwythonRateLimitError,TwythonAuthError
import json
import pymysql
import time
con = pymysql.connect(user='root', password = '', database='ngo_datamining', charset='utf8')
cur = con.cursor()
print "SQL connected"

#This is your Twitter application details
APP_KEY = 'n4q4855QmAGgJeyzCYVnO3KTx'
APP_SECRET =  'oHi4zAbIXMCyzxp22RnqPcHpjIWntipS4R2i4yLLoMfQF0X0d2'
OAUTH_TOKEN = '739770952762855427-uJBBK8NCtu1x89zn0Q7X9nQ30Q1diXX'
OAUTH_TOKEN_SECRET = 'mzUbHuUNFym8w5O4mmgVmYtWDMMSX9DMtctX71T9RW8W6'

# Requires Authentication as of Twitter API v1.1
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
print "Authorization is complete"

#PHASE1- PHASE1 (users from twitter)
#PHASE2- PHASE2 (distinct users from phase 1)
#PHASE3- PHASE3 (data from username)
#TABLE CREATION 
#~~~RAW USER DATA
sql_create_table = "CREATE TABLE IF NOT EXISTS PHASE1(tweet_id varchar(50), user_id varchar(50), screen_name varchar(50), text varchar(500),keyword varchar(25),main_key varchar(25),followers_count integer,location varchar(50),profile_pic varchar(200), is_retweeted varchar(10), retweet_count integer)"
cur.execute(sql_create_table)
con.commit()
#~~~Distinct screen_names into database table
query="CREATE TABLE IF NOT EXISTS PHASE2(id MEDIUMINT NOT NULL AUTO_INCREMENT,screen_name VARCHAR(50) NOT NULL,keyword varchar(50),main_key varchar(50),PRIMARY KEY (id)) " 
cur.execute(query)
con.commit()
#~~~PROFILE data from user list
sql_create_table = "CREATE TABLE IF NOT EXISTS PHASE3(tweet_id varchar(50), user_id varchar(50), screen_name varchar(50), text varchar(500),keyword varchar(25),main_key varchar(25),location varchar(50),is_retweeted varchar(10), retweet_count integer)"
cur.execute(sql_create_table)
con.commit()
print "PHASE1 table created"
print "PHASE2 table created"
print "PHASE3 table created"


#TRUNCATING TABLES
#truncate table PHASE1  list
trunc_table="truncate table PHASE1"
cur.execute(trunc_table)
con.commit()

#truncate table   PHASE2
trunc_table="truncate table PHASE2"
cur.execute(trunc_table)
con.commit()

#truncate table "RAW" PHASE3
trunc_table="truncate table PHASE3"
cur.execute(trunc_table)
con.commit()

print "TABLES TRUNCATED"
word="ANIMAL"


if word=="CHILD":
	i=1
	end=7
elif word=="HEALTH":
	i=8
	end=16
elif word=="ANIMAL":
	i=17
	end=24
elif word=="WOMEN":
	i=25
	end=32
elif word=="WOMEN":
	i=33
	end=44
	
i=1
end=44
#Finding tweets from keywords 

print "RECENT TWEETS"
while i<=end:
	
    		#KEYWORDS is the name of table that contains the keyword list
	cur.execute("select keyword from KEYWORDS where id=%s",(i))
	con.commit()
	row_data = cur.fetchall()
	print row_data[0]
	
	cur.execute("select KEYWORDS.key from KEYWORDS where id=%s ",(i))
	con.commit()
	row1_data = cur.fetchall()
	print row1_data[0]
	print '\n'
	#seaching for the keyword
	user_tweets = twitter.search(q="%s"%row_data[0],result_type='recent',lang='en', count=100)
	
	j=0
	#parse the tweets
	for tweet_item in user_tweets['statuses']:
		tweet_id = tweet_item['id']
		user_id =  tweet_item['user']['id']
		screen_name = tweet_item['user']['screen_name']
		text =  tweet_item['text']
		followers_count= tweet_item['user']['followers_count']
		location = tweet_item['user']['location']
		profile_pic = tweet_item['user']['profile_image_url']
		is_retweeted =  tweet_item['retweeted']
		retweet_count = tweet_item['retweet_count']
		print screen_name
		print '\n'
		
		sql_insert = "INSERT IGNORE INTO PHASE1(tweet_id, user_id, screen_name, text, keyword,main_key,followers_count,location,profile_pic,is_retweeted, retweet_count) values (%s, %s, %s, %s, %s, %s, %s ,%s ,%s, %s, %s)"
		cur.execute(sql_insert, (tweet_id, user_id, screen_name, text ,row_data[0],row1_data[0],followers_count,location,profile_pic, is_retweeted, retweet_count) )
		con.commit()
		j=j+1
		print "RECORD INSERTED"
	
	#find the number of results from the keyword and update it to table KEYWORDS
	cur.execute("UPDATE KEYWORDS SET count=%s WHERE id = %s",(j,i))
	con.commit()
	print i
	i=i+1

#Distinct screen_names into database table

query="INSERT INTO PHASE2(screen_name,keyword ,main_key) select DISTINCT screen_name,keyword,main_key from PHASE1 "
cur.execute(query)
con.commit()

query="select * from PHASE2"
cur.execute(query)
con.commit()
total_user_data=cur.fetchall()

query="select count(*) from PHASE2"
cur.execute(query)
con.commit()
count=cur.fetchall()
print count


i=1

print "finding tweets from profiles"
while i<count:
	try:	
		cur.execute("select screen_name from PHASE2 where id=%s",(i));
		con.commit()
		name=cur.fetchall()
		cur.execute("select main_key from PHASE2 where id=%s",(i));
		con.commit()
		main_key=cur.fetchall()
		cur.execute("select keyword from PHASE2 where id=%s",(i));
		con.commit()
		keyword=cur.fetchall()
		user_tweets = twitter.get_user_timeline(screen_name="%s"%name[0],count=100,exclude_replies='true')
	
		for tweet_item in user_tweets:
		
			tweet_id = tweet_item['id']
			user_id =  tweet_item['user']['id']
			screen_name = tweet_item['user']['screen_name']
			text =  tweet_item['text']
			#location,follower_count,profile pic,
			location = tweet_item['user']['location']
			is_retweeted =  tweet_item['retweeted']
			retweet_count = tweet_item['retweet_count']
			
			print screen_name
			print '\n'
			try:
				sql_insert = "INSERT IGNORE INTO PHASE3(tweet_id, user_id, screen_name, text, keyword, main_key,location,is_retweeted, retweet_count) values (%s, %s, %s, %s, %s, %s, %s ,%s ,%s)"
				cur.execute(sql_insert, (tweet_id, user_id, screen_name, text ,keyword[0],main_key[0],location, is_retweeted, retweet_count) )
				con.commit()
				print "record inserted"
			except: pass
		i=i+1
		print "USER TILL NOW =%s"%(i)
		print '\n'
		
	except TwythonRateLimitError, e:
		print "[Exception Raised] Rate limit exceeded"
		reset = int(twitter.get_lastfunction_header('x-rate-limit-reset'))
		wait = max(reset - time.time(), 0) + 10 # addding 10 second pad
	#twitter.disconnect()
		print wait
		time.sleep(wait)
		continue
	
	except TwythonAuthError, e:
		print e
		print "Non rate-limit exception encountered. Sleeping for 1 min before retrying"
		#time.sleep(60*1)
		print time.localtime()
		i=i+1
		continue
	except :
		 pass
		 i=i+1
		
	
print "end"

												
sql_create_table = "CREATE TABLE IF NOT EXISTS DISTINCT_RELEVANT_TWEETS(tweet_id varchar(25), user_id varchar(25), screen_name varchar(25), text varchar(200))"
cur.execute(sql_create_table)
con.commit()
print "DISTINCT_animal_tweets table created \n"
trunc_table="TRUNCATE table DISTINCT_RELEVANT_TWEETS"
cur.execute(trunc_table)
con.commit()

#word="ANIMAL"
#if word=="CHILD":

	#query_sql="INSERT IGNORE INTO DISTINCT_RELEVANT_TWEETS(tweet_id, user_id, screen_name, text) SELECT tweet_id, user_id, screen_name, text FROM PHASE3 WHERE text like '%%''%%''%%''%%''%%''%%''%%''%%''%%''%%''%%''%%''%%''%%''%%''%%''%%''%%'

#elif word=="HEALTH":

query_sql="INSERT IGNORE INTO DISTINCT_RELEVANT_TWEETS(tweet_id, user_id, screen_name, text) SELECT tweet_id, user_id, screen_name, text FROM PHASE3 WHERE text like '%yoga day%' OR text LIKE '%mental health issue%' OR text LIKE '%hetrosexualPrideday%' OR text LIKE '%bad mood%'OR text LIKE '%suicide%'OR text LIKE  '%yoga day%'OR text LIKE '%homeopathy%'OR text LIKE '%cure cancer%'OR text LIKE '%genetic disease%'OR text LIKE '%fighting diseases%'OR text LIKE '%fighting kidney and urinary diseases%'OR text LIKE '%fighting viral diseases%'OR text LIKE '%global health%'OR text LIKE '%fighting infectious diseases%'OR text LIKE '%protect against brain diseases%'OR text LIKE '%WHO%'OR text LIKE '%fighting drugs and diseases%'OR text LIKE '%repiratory diseases%'OR text LIKE'%neurological diseases%'OR text LIKE'%fighting cholera and water-born diseases%'OR text LIKE'%fighting HIV/Aids%'OR text LIKE'%ALS ice bucket challenge%'OR text LIKE'%awareness for ALS%'OR text LIKE'%meditation%'OR text LIKE'%malnutrition%'OR text LIKE'%asthma%'OR text LIKE'%Tuberculosis and Malaria%'OR text LIKE'%Global Health Council%'OR text LIKE'% urinary tract infections%'OR text LIKE'%heart diseases%'OR text LIKE'%Depression%'OR text LIKE'%Loneliness%'OR text LIKE'%Sociability%' "
cur.execute(query_sql)
con.commit()

#elif word=="ANIMAL": 

query_sql="INSERT IGNORE INTO DISTINCT_RELEVANT_TWEETS(tweet_id, user_id, screen_name, text) SELECT tweet_id, user_id, screen_name, text FROM PHASE3 WHERE text like '%animalwelfare%' OR text LIKE '%doglover%' OR text LIKE '%govegan%' OR text LIKE '%animal care%' OR text LIKE '%animals killed%' OR text LIKE '%protect animals%' OR text like '%animal rescue%' OR text LIKE '%petlover%' OR text LIKE '%petloss%' OR text LIKE '%bantrophyhunting%' OR text LIKE '%slaughter%'OR text LIKE '%animalabuse%'OR text LIKE '%#animalcrueality%'OR text LIKE '%animal adopt%'OR text LIKE '%animalhelp%'OR text LIKE '%animalrights%'OR text LIKE '%animalkilled%'OR text LIKE '%animal curelty%'OR text LIKE '%animal shelter%'OR text LIKE '%animal shelter%'OR text LIKE '%animal lovers%'OR text LIKE '%animal abuse%'OR text LIKE '%animal care%'OR text LIKE '%animal friendly%'OR text LIKE '%animal charities%'OR text LIKE '%animal activists%'OR text LIKE '%animal welfare%'OR text LIKE '%animal torturing%'  '%stop animal testing%'  '%rescue animals%'  '%animal foundation%'  '%protectanimals%'  '%helpanimals%'  '%save the animals%'"
cur.execute(query_sql)
con.commit()
#elif word=="WOMEN":
	
query_sql="INSERT IGNORE INTO DISTINCT_RELEVANT_TWEETS(tweet_id, user_id, screen_name, text) SELECT tweet_id, user_id, screen_name, text FROM PHASE3 WHERE text like '%educating women%' OR text LIKE '%educating girls%' OR text LIKE  '%domesticviolence%' OR text LIKE '%empowergirls%' OR text LIKE '%empowerwomen%'OR text LIKE  '%womenequality%' OR text LIKE '%women suffering%' OR text LIKE '%acidattackvictim%' OR text LIKE  '%adopt a girl%' OR text LIKE '%gender discrimination%'OR text LIKE  '%rape victim%' OR text LIKE  '%help women%'OR text LIKE  '%womeninneed%' OR text LIKE'%helpingwomen%'OR text LIKE '%women abused%'OR text LIKE '%girl abused%' OR text LIKE'%women in rehab%' OR text LIKE '%woman beaten%'OR text LIKE '%woman depressed%'OR text LIKE '%torturedwoman %'OR text LIKE '%careforwomen%'OR text LIKE '%helpwomen%'OR text LIKE '%womenrights%'OR text LIKE '%YesAllWomen%'OR text LIKE '%everydaysexism%'OR text LIKE '%standforwomen%'OR text LIKE '%women body shamed%'OR text LIKE '%women raped%'OR text LIKE '%childmarriage%'OR text LIKE '%endchildmarriage%' OR text LIKE '%endgenderbasedviolence%' OR text LIKE '%EndViolenceAgainstWomenAndGirls%' OR text LIKE '%woman thrashed%'OR text LIKE '%waronwomen%' OR text LIKE '%women harrassed%' OR text LIKE '%women faught%' OR text LIKE '%unemployed women%' OR text LIKE'%woman bullyied%'OR text LIKE '%girl bullyied%' OR text LIKE'%girl assaulted%'OR text LIKE '%careforgirls%' OR text LIKE '%women attempted suicide%' OR text LIKE '%girl attempted suicide%' OR text LIKE '%girls literacy%' "
cur.execute(query_sql)
con.commit()
#elif word=="OLDAGE":
	
query_sql="INSERT IGNORE INTO DISTINCT_RELEVANT_TWEETS(tweet_id, user_id, screen_name, text) SELECT tweet_id, user_id, screen_name, text FROM PHASE3 WHERE text like '%ElderAbuseAwarenessDay%' OR text LIKE '%OlderAmericansMonth%'OR text LIKE '%OlderAdults%' OR text LIKE '%Financial abuse of elderly%' OR text LIKE '%elder abuse prevention%' OR text LIKE '%older women%' OR text LIKE'%pensioners%'OR text LIKE '%carehomes for elderly%' OR text LIKE '%WEAAD%'OR text LIKE '%AgeUK%'OR text LIKE '%stop ritual abuse%'OR text LIKE '%Psyco therapy%'OR text LIKE '%mind control%'OR text LIKE '%victims%'OR text LIKE '%workers%'OR text LIKE '%against conservation%'OR text LIKE '%old age%'OR text LIKE '%violence%'OR text LIKE '%death penalty%'OR text LIKE '%freedom%'OR text LIKE '%crime on humanity%'OR text LIKE '%stay safe%'OR text LIKE '%die%'OR text LIKE '%grand dad %'OR text LIKE '%appalled%' OR text LIKE '%old age home%' OR text LIKE '%the earth saviors foundations%' OR text LIKE'%nursing home%'OR text LIKE '%throwing parents%' OR text LIKE'%homeless abandoned senior citizens%' OR text LIKE '%Ayurda%' OR text LIKE '%generosity and big hearted donation%'OR text LIKE '%Depression%'"
cur.execute(query_sql)
con.commit()




sql_create_table1 = "CREATE TABLE IF NOT EXISTS DISTINCT_RELEVANT_COUNT(screen_name varchar(25), count int)"
cur.execute(sql_create_table1)
con.commit()
print "DISTINCT_RELEVANT_COUNT table created \n"

trunc_table="truncate table DISTINCT_RELEVANT_COUNT"
cur.execute(trunc_table)
con.commit()


query_sql1="INSERT IGNORE INTO DISTINCT_RELEVANT_COUNT(screen_name, count) SELECT screen_name,COUNT(*) as count FROM DISTINCT_RELEVANT_TWEETS GROUP BY screen_name;"
cur.execute(query_sql1)
con.commit()
print "DISTINCT_RELEVANT_COUNT table data inserted \n"

sql_create_table = "CREATE TABLE IF NOT EXISTS INTEREST_INDEX(`screen_name` VARCHAR(50) NOT NULL , `total_tweet` INT(10))"
cur.execute(sql_create_table)
con.commit()

trunc_table="TRUNCATE table INTEREST_INDEX"
cur.execute(trunc_table)
con.commit()
print "truncate table INTEREST_INDEX done\n"

sql_create_table = "INSERT INTO INTEREST_INDEX(screen_name,total_tweet) SELECT screen_name, count(screen_name) FROM PHASE3 GROUP BY screen_name"
cur.execute(sql_create_table)
con.commit()

sql_create_table1 = "CREATE TABLE IF NOT EXISTS INTEREST_PERCENT(screen_name varchar(25), total_tweet int,relevant int,percent float)"
cur.execute(sql_create_table1)
con.commit()
print "INTEREST_PERCENT table created \n"

trunc_table="truncate table INTEREST_PERCENT"
cur.execute(trunc_table)
con.commit()

sql="INSERT INTO `INTEREST_PERCENT`(`screen_name`, `total_tweet`, `relevant`) SELECT a.screen_name ,b.total_tweet , a.count from DISTINCT_RELEVANT_COUNT a INNER JOIN INTEREST_INDEX b ON a.screen_name=b.screen_name"
cur.execute(sql)
con.commit()
print "INTEREST_PERCENT data entered \n"

sql3="UPDATE `INTEREST_PERCENT` SET percent=(relevant/total_tweet)*100"
cur.execute(sql3)
con.commit()

drop_table1="DROP table INTEREST_INDEX"
cur.execute(drop_table1)
con.commit()

drop_table2="DROP table DISTINCT_RELEVANT_COUNT"
cur.execute(drop_table2)
con.commit()

print "FINISH !!!!!!!"
cur.close()
con.close()
#user_tweets = twitter.get_user_timeline(screen_name='LoriHandrahan2',count=200)
#twitter.send_direct_message(screen_name="bhardwajsona1", text= ' hello! this is from python ')
print time.localtime()
#time 1:30 -----

