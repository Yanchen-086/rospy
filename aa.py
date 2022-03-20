




from myrospy import rospy
import logging
import logging.config

#string="chatter"

#print(rospy.init_node("talker", True))
#print(rospy.Publisher("chatter",string))
#print(rospy.get_time())
#print(rospy.is_shutdown())

#str="helloworld"
#print(rospy.loginfo(str))
#print(rospy.publish(str))
#print(rospy.sleep())rospy.sleep())
#print(rospy.sleep()rospy.sleet())



#data="aa"
#rospy.loginfo('I heard')
#print(rospy.init_node("chatter"))

#logging.config.fileConfig('python_logging.config')
#logger=logging.getLogger(name='log')
rospy.init_node('log',anonymous=False)
 logging.debug('this is debug message')  
 logging.info('this is info message')  
 logging.warning('this is warning message') 


rospy.loginfo('I')

#logger.debug('msg')
#logger.info('msg')





##print(rospy.Subscriber("chatter", str))
##print(rospy.spin())




















