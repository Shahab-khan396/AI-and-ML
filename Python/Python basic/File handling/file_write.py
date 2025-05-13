st='''dear sir,
                with due respect it is stated that i am suffering from fever last night,
kindly grant me leave for 1 year.i shall be very thanksfull to you for this. 
                            Thank you, 
                                                            Your obediently,
                                                            shahab khan,
                                                            roll no: 2213'''
f=open("myfile.txt","w","r")
d=f.read()
print(d)
f.write(st)
f.close()

