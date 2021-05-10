(define (problem p7)
(:domain test)
(:objects 
   r - room h - heater w - window l - light p - occupancy)
(:init 
    (presence p)
    (open w)
    (= (temp r) 17.9)
    (= (air-quality r) 421)
    (= (luminance r) 326)
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
