class lms():

    def __init__(self,p_loan_rules_tuple,p_cust_name,p_cust_cs,p_cust_loan_amt):
            self.p_loan_rules_tuple = p_loan_rules_tuple
            self.p_cust_name= p_cust_name
            self.p_cust_cs=p_cust_cs
            self.p_cust_loan_amt=p_cust_loan_amt
           

    def lms_engine(self):
        l_result = {}
        l_result["CustomerName"] = self.p_cust_name
        l_result["CustomerCS"] = self.p_cust_cs
        l_result["CustomerLoanAmt"] = self.p_cust_loan_amt
        l_success_flg = 0
        for rule in self.p_loan_rules_tuple:
            if self.p_cust_cs >= rule["CSStart"] and self.p_cust_cs <= rule["CSEnd"] and self.p_cust_loan_amt >= rule["LoanAmtStart"] and self.p_cust_loan_amt <= rule["LoanAmtEnd"]:
                l_success_flg = 1
                l_result["InterestPercent"] = rule["InterestPercent"]
                l_result["DurationInMonths"] = rule["DurationInMonths"]
                l_result["LoanStatus"] = "Approved"
                # l_result["Message"] = 
                break

        if l_success_flg == 0:
            # l_result["Message"] = 
            l_result["LoanStatus"] = "Rejected"

        return l_result

