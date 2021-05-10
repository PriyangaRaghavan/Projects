(define (problem p15)
(:domain test)
(:objects 
   r - room h - heater w - window l - light p - occupancy)
(:init 
    (open w)
    (presence p)
    (= (temp r) 22.4)
    (= (air-quality r) 424)
    (= (luminance r) 271)
)
(:goal 
      (and
         (>= (temp r) 20)
         (<= (temp r) 24)
         (>= (luminance r) 400)
         (>= (air-quality r) 450)
         (< (air-quality r) 800)
         
           
      ) 
          
)
) 
