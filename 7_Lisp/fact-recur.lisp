(defun factorial (n)
    (if (= n 0)
        1
        (* n (factorial (- n 1)))))
(setq i (read))

(format t "~D! = ~D~%" i (factorial i))