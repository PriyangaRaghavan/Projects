(define (problem p29)
(:domain test)
(:objects 
   r - room h - heater w - window l - light p - occupancy)
(:init 
    (open w)
    (= (temp r) 20.1)
    (= (air-quality r) 328)
    (= (luminance r) 539)
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
