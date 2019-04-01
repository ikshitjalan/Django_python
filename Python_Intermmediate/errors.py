try:
    f= open("simple.txt",'r')
    f.write("Test text to be written")

except :
    print("Error: Could not read or write file")
finally:
    print("success in finally keyword doesnot depend upon error ")
