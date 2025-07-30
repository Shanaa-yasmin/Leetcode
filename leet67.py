a=input("Enter the binary number")
b=input("Enter the binary number")
i,j=len(a)-1,len(b)-1
carry=0
result = []                    # to build the answer

while i >= 0 or j >= 0 or carry:
	total = carry              # start with carry from previous step

        # add current bit of 'a' if available
	if i>=0:
            total += int(a[i])
            i -= 1

        # add current bit of 'b' if available
	if j >= 0:
            total += int(b[j])
            j -= 1
        
        # Current bit = total % 2 (because binary only 0 or 1)
	result.append(str(total % 2))

        # Update carry = total // 2 (because if total is 2, carry is 1)
	carry = total // 2

    # Reverse result because we built it from LSB to MSB
print("".join(reversed(result)))
