import lms_master_data as md

class lms():
    

    def __init__(self,p_loan_rules_tuple,p_cust_name,p_cust_cs,p_cust_loan_amt):
            self.p_loan_rules_tuple = p_loan_rules_tuple
            self.p_cust_name= p_cust_name
            self.p_cust_cs=p_cust_cs
            self.p_cust_loan_amt=p_cust_loan_amt
           

    def lms_engine(self):
        self.l_result = {}
        self.l_result["CustomerName"] = self.p_cust_name
        self.l_result["CustomerCS"] = self.p_cust_cs
        self.l_result["CustomerLoanAmt"] = self.p_cust_loan_amt
        l_success_flg = 0
        for rule in self.p_loan_rules_tuple:
            if self.p_cust_cs >= rule["CSStart"] and self.p_cust_cs <= rule["CSEnd"] and self.p_cust_loan_amt >= rule["LoanAmtStart"] and self.p_cust_loan_amt <= rule["LoanAmtEnd"]:
                l_success_flg = 1
                self.l_result["InterestPercent"] = rule["InterestPercent"]
                self.l_result["DurationInMonths"] = rule["DurationInMonths"]
                self.l_result["LoanStatus"] = "Approved"
                # l_result["Message"] = 
                break

        if l_success_flg == 0:
            # l_result["Message"] = 
            self.l_result["LoanStatus"] = "Rejected"

        return self.l_result

