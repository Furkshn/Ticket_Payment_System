import time
import datetime
from timeit import default_timer as timer
import qrcode
import cv2
import random



class Bus_ticket_systems():

    student_pay = 1.50
    full_fare = 2.75

    connecting_ticket_for_student = 0.25
    connecting_ticket_for_fullfare = 0.75


    def __init__(self,card_number,balance,person):

        self.card_number = card_number
        self.balance = balance
        self.person = person



    def paying_ticket(self):


        if self.balance == 0:

            return f"Insufficient Balance !"


        if self.person == "Student":

            if self.balance >= Bus_ticket_systems.student_pay:

                self.balance -= Bus_ticket_systems.student_pay
                return f"Available Balance: {self.balance}"

            else:
                return f"Please Load Enough Money To Your Card !"


        elif self.person == "Full_fare":

            if self.balance >= Bus_ticket_systems.full_fare:

                self.balance -= Bus_ticket_systems.full_fare
                return f"Available Balance: {self.balance}"

            else:
                return f"Please Load Enough Money To Your Card !"




    def connecting_paying(self):

        if self.balance == 0:

            return f"Insufficient Balance !"


        if self.person == "Student":

            if self.balance >= Bus_ticket_systems.connecting_ticket_for_student:

                self.balance -= Bus_ticket_systems.connecting_ticket_for_student
                return f"Available Balance: {self.balance}"

            else:
                return f"Please Load Enough Money To Your Card !"


        elif self.person == "Full_fare":

            if self.balance >= Bus_ticket_systems.connecting_ticket_for_fullfare:

                self.balance -= Bus_ticket_systems.connecting_ticket_for_fullfare
                return f"Available Balance: {self.balance}"

            else:
                return f"Please Load Enough Money To Your Card !"



    def load_money_to_card(self,amount):

        self.balance += amount
        print(".")
        time.sleep(0.3)
        print("..")
        time.sleep(0.3)
        print("...")

        return  f"""{amount} TL has been loaded on your card.
                Total Balance is {self.balance} Tl.

                               We wish you a good trip..."""



    def pay_with_QR_code(self):

        qr = qrcode.QRCode(                  # Generating qr code for passenger's payment
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4)

        data_for_qrcode = str(random.choice(range(1000))) + str(random.choice(range(1000))) +str(self.card_number) + str(self.person)
        qr.add_data(data_for_qrcode)
        qr.make(fit=True)


        qrcode_img = qr.make_image(fill_color="black", back_color="white")
        qrcode_file_name = str(random.choice(range(1000))) + str(random.choice(range(1000))) +str(self.card_number) + str(self.person)
        qrcode_img.save(f"{qrcode_file_name}.png")

        print(".")
        time.sleep(0.3)
        print("..")
        time.sleep(0.3)
        print("...")
        print("QR Code Created !")


        image = cv2.imread(f"{qrcode_file_name}.png")

        cv2.imshow(f"{qrcode_file_name}", image)



        # Camera in bus system validate paying process

        cap = cv2.VideoCapture(0)

        detector = cv2.QRCodeDetector()

        while True:

            _, img = cap.read()
            cv2.imshow("QR Code Decode",img)
            data, vertices_array, _ = detector.detectAndDecode(img)

            if vertices_array is not None:

                if data == data_for_qrcode and data_for_qrcode == qrcode_file_name:

                    print("QR DETECTED ! ")
                    print(self.paying_ticket())
                    break

                else:

                    print("QR Code Payment does not match data...")
                    continue

            else:

                print("QR Code Payment Processing...")
                continue

        cap.release()
        cv2.destroyAllWindows()



payment = Bus_ticket_systems(120,15,"Student")

