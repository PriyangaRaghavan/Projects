(define (problem p20)
(:domain test)
(:objects 
   r - room h - heater w - window l - light p - occupancy)
(:init 
    (presence p)
    (= (temp r) 23.1)
    (= (air-quality r) 629)
    (= (luminance r) 290)
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
