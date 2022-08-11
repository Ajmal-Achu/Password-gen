/* Copy Right Credits 2022 @AJMAL
https://github.com/Ajmal-Achu*/

import random

// values

let lower = "abcdefghijklmnopqrstuvwxyz"
let upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
let number = "123456789"
let symbol = "!@3$%^&*+?,_"

// values ends here

// random password genarator

all =lower + upper + number + symbol
length = 11
password = "".join(random.sample(all,length))


print(" THE RANDOMLY GENARATED PASSWORD IS :" + password)
