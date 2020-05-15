(princ "Enter length of list: ")
(setq x (read))
(setq y (list))
(loop for i from 0 to (- x 1)
    do(
        setq y (append y (list(read)))
    )
)
(princ "Enter value of n: ")
(setq n (read))
(format t "Element ~D of list is: ~D" n (nth n y))  


