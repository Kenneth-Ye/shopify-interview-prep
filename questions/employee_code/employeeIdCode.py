import sys

class EmployeeIdVerification:
    NOT_VALID_OUTPUT = "INVESTIGATE"
    VALID_OUTPUT = "PASS"

    def verifyId(self, first_name, last_name, id_code):
        # check that first 2 chars of id_code match first two letters of lastname
        if (last_name[:2].upper() != id_code[:2]):
            print(self.NOT_VALID_OUTPUT)
            return
            # print whatever code for lastname char error
        # check that 2 chars of id_code match first two letters of firstname
        elif (first_name[:2].upper() != id_code[2:4]):
            print(self.NOT_VALID_OUTPUT)
            return


        numeric_part = id_code[4:12]
        verification_digit = int(id_code[-1])

        even_sum = 0
        odd_sum = 0
        # calculate the even positiuon sum and odd position sum
        for i in range(len(numeric_part)):
            if (i+1 % 2 == 0):
                even_sum += int(numeric_part[i])
            else:
                odd_sum += int(numeric_part[i])
        diff = abs(even_sum - odd_sum) % 10
        if (diff == verification_digit):
            print(self.VALID_OUTPUT)
        else:
            print(self.NOT_VALID_OUTPUT)




if __name__ == "__main__":
    cmd_line_args = sys.argv[1:]
    first_name = cmd_line_args[0]
    last_name = cmd_line_args[1]
    id_code = cmd_line_args[2]
    verifier = EmployeeIdVerification()
    verifier.verifyId(first_name, last_name, id_code)