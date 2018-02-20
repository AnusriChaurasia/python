import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("anusricc8@gmail.com","nikki2808")
msg="did u get?"
s.sendmail("anusricc8@gmail.com","anulekha2112016@gmail.com,anitharathnam.kv2gmail.com",msg)
print("success")
s.quit()
