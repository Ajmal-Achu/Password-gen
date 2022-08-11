/*Copy Right © 2022 @AJMAL
 https://github.com/Ajmal-Achu*/

import random

// values

let lower = "abcdefghijklmnopqrstuvwxyz"
let upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
let number = "123456789"
let symbol = "!@3$%^&*+?,_"

// values ends here

// random password genarator

ajmal =lower + upper + number + symbol
charactes = 11
password = "".join(random.sample(ajmal,characters))


print(" THE RANDOMLY GENARATED PASSWORD IS :" + password)
