class shopping():

    # Class Variables
    g_cart = []
    g_cart_entry = {}
    g_cust_id = None
    c_products = [{"prodId":1,"productName":"Fruit","UnitPrice":2}
                 ,{"prodId":2,"productName":"Stationary","UnitPrice":5}
                 ,{"prodId":3,"productName":"Cleaning supplies","UnitPrice":3}
                 ,{"prodId":4,"productName":"Auto-oil","UnitPrice":8}
                 ]
    # g_cart = [{2: 10}, {1: 3}, {3: 1}, {4: 7}]

    # Class Functions
    def show_products(self):
        print(self.c_products)

    def add_to_cart(self,p_prodId,p_qty):
        self.g_cart_entry[p_prodId] = p_qty
        self.g_cart.append(self.g_cart_entry)
        self.g_cart_entry = {}

    def show_cart(self):
        print(self.g_cart)

    def generate_invoice_total(self):
        total=0
        for i in self.g_cart:
            print("My i of g_cart -->",i)
            #print("------------------")
            for j in self.c_products:
                print(" My j of c_produts -->",j)
                if list(i)[0] == j["prodId"]:
                    print("I am in if --> ",j["UnitPrice"])
                    total = total + j["UnitPrice"]* i[j["prodId"]]
                    
        print("Total Invoice:", total)


# Create Object
# #############################################
#  Shopper 1
s1 = shopping()
#s1.show_products()
s1.add_to_cart(2,10)
#s1.show_cart()
s1.add_to_cart(1,3)
#s1.show_cart()
s1.add_to_cart(3,1)
#s1.show_cart()
s1.add_to_cart(4,7)
s1.show_cart()
print("++++++++++++++++++++++++++++++")

s1.generate_invoice_total()