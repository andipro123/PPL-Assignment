(defun factorial (n)
    (setq ans 1)
    (loop for i from 1 to n
        do(setq ans (* ans i)))
    ans)
(setq i (read))

(format t "~D! = ~D~%" i (factorial i))