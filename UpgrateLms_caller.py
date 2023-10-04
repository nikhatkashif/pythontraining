import lms_master_data as md
import UpgradeLms_engine as lms

# Test Master Data
# ##############################
# for rule in md.loan_rules_tuple:
#   print(rule)

# Supply Input Customer Data
# ##############################
'''
l_cust_name = "AA"
l_cust_cs = 233
l_cust_loan_amt = 2334

# Call the LMS Engine
# #############################

l_result = lms.lms_engine(p_loan_rules_tuple = md.loan_rules_tuple
                         ,p_cust_name = l_cust_name
                         ,p_cust_cs = l_cust_cs
                         ,p_cust_loan_amt = l_cust_loan_amt)

'''
c1 = lms.lms(md.loan_rules_tuple,"Nikhat",125,9009)
c1_loan=c1.lms_engine()
print(c1_loan) 

c2 = lms.lms(md.loan_rules_tuple,"Kashif",340,30009)
c2_loan=c2.lms_engine()
print(c2_loan) 

c3 = lms.lms(md.loan_rules_tuple,"Nikhat",550,20009)
print(c3.lms_engine())
