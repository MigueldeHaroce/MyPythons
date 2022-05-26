from itertools import zip_longest


class Objects:
    ledger = []
    amount = 100
    amount_to_withdraw = -abs(20)
    tranfer_amount = -abs(20)
    amount_to_withdraw2 = -abs(50)

    description = "deposit"
    wd_description = "food"
    wd_description2 = "hotel"
    tranfer_description = "clothes"

    deposit = {"Amount": amount, "Description": description}
    ledger.append(deposit["Amount"])
    withdraw = {"Amount": amount_to_withdraw, "Description": wd_description}
    withdraw2 = {"Amount": amount_to_withdraw2, "Description": wd_description2}

    if withdraw["Amount"] >= amount:
        happened = False
    else:
        ledger.append(withdraw["Amount"])
        happened = True
    transfer = {"Amount": tranfer_amount, "Description": tranfer_description}
    if withdraw2["Amount"] >= amount:
        happened2 = False
    else:
        ledger.append(withdraw2["Amount"])
        happened2 = True
    if transfer["Amount"] >= amount:
        happened3 = False
    else:
        ledger.append(transfer["Amount"])
        happened3 = True

    check_funds1 = amount_to_withdraw + tranfer_amount + amount_to_withdraw2
    check_funds = amount + check_funds1
    ledger.append(check_funds)

    @classmethod
    def show_objects(cls):
        print("*************Food*************")
        print(cls.description + "           " + str(cls.amount))
        print(cls.wd_description + "                      " +
              str(cls.amount_to_withdraw))
        print(cls.wd_description2 + "                     " +
              str(cls.amount_to_withdraw2))
        print(cls.tranfer_description + "                   " +
              str(cls.tranfer_amount))
        print(f"Total:  {cls.check_funds}")

    percentage_of_wd1 = int(amount_to_withdraw) / int(amount) * 100
    percentage_of_wd = abs(percentage_of_wd1)
    first_per = {"%": percentage_of_wd}
    percentage_of_wd3 = abs(int(amount_to_withdraw2) / int(amount) * 100)
    percentage_of_trans_amount = abs(int(tranfer_amount) / int(amount) * 100)

    @classmethod
    def create_spend_chart(cls):
        print("...............................................")
        chart = ""
        for i in range(100, -1, -10):
            if cls.percentage_of_wd >= int(i) or cls.percentage_of_wd3 >= int(i) or cls.percentage_of_trans_amount >= int(i):
                if cls.percentage_of_trans_amount >= int(i) and  cls.percentage_of_wd >= int(i) and cls.percentage_of_wd3 >= int(i):
                    chart += f"{str(i) + '| ':>4}o   o   o\n"
                elif cls.percentage_of_trans_amount >= int(i) and cls.percentage_of_wd3 >= int(i):
                    chart += f"{str(i) + '| ':>4}   o   o\n"
                elif cls.percentage_of_trans_amount >= int(i) and cls.percentage_of_wd >= int(i):
                    chart += f"{str(i) + '| ':>4}o       o\n"
                elif cls.percentage_of_wd >= int(i) and cls.percentage_of_wd3 >= int(i):
                    chart += f"{str(i)+'| ':>4}o   o   \n"
                elif cls.percentage_of_wd3 >= int(i):
                    chart += f"{str(i)+'| ':>4}    o   \n"
                elif cls.percentage_of_trans_amount >= int(i):
                    chart += f"{str(i)+'| ':>4}       o\n"
                elif cls.percentage_of_wd >= int(i):
                    chart += f"{str(i)+'| ':>4}o\n"
            elif cls.percentage_of_wd < int(i) or cls.percentage_of_wd3 < int(i) or cls.percentage_of_trans_amount < int(i):
                chart += f"{str(i) + '|'}\n"
        return chart

    @classmethod
    def final(cls):
        print("Percentage spent by category")
        print(cls.create_spend_chart())
        print("    ----------")

        a = "`"
        b = cls.wd_description
        c = cls.wd_description2
        d = cls.tranfer_description
        text = f"{a} {b} {c} {d}"
        for x in zip_longest(*text.split(), fillvalue=" "):
            print("   ".join(x))
run = Objects
run.show_objects()
run.create_spend_chart()
run.final()
