(defun c:ChandelierBulbs (/ num-bulbs-x num-bulbs-y spacing-x spacing-y bulb-diameter height amplitude center-x center-y center-z x y z i j sphere)
  ;; Get user inputs
  (setq num-bulbs-x (atoi (getstring "Enter the number of bulbs in X direction: ")))
  (setq num-bulbs-y (atoi (getstring "Enter the number of bulbs in Y direction: ")))
  (setq spacing-x (atof (getstring "Enter the spacing of bulbs in X direction (mm): ")))
  (setq spacing-y (atof (getstring "Enter the spacing of bulbs in Y direction (mm): ")))
  (setq bulb-diameter (atof (getstring "Enter the bulb diameter (mm): ")))
  (setq height (atof (getstring "Enter the height of the chandelier (mm): ")))

  ;; Calculate amplitude and center offset
  (setq amplitude (/ height 4))
  (setq center-z (/ height 2))

  ;; Loop through bulbs and create spheres
  (setq i 0)
  (while (< i num-bulbs-x)
    (setq j 0)
    (while (< j num-bulbs-y)
      ;; Calculate X, Y, Z positions
      (setq x (- (* i spacing-x) (/ (* (1- num-bulbs-x) spacing-x) 2)))
      (setq y (- (* j spacing-y) (/ (* (1- num-bulbs-y) spacing-y) 2)))
      (setq z (+ center-z (* amplitude (sin (/ (* x 3.14159265358979) (* num-bulbs-x spacing-x)))
                                     (cos (/ (* y 3.14159265358979) (* num-bulbs-y spacing-y))))))

      ;; Create sphere at calculated position
      (command "_sphere" (list x y z) (/ bulb-diameter 2))

      ;; Increment Y direction
      (setq j (1+ j))
    )
    ;; Increment X direction
    (setq i (1+ i))
  )
  (princ "\nChandelier bulbs created!")
)
