(define (problem p17)
(:domain test)
(:objects 
   r - room h - heater w - window l - light p - occupancy)
(:init 
    (presence p)
    (on_heater h)
    (= (temp r) 22.2)
    (= (air-quality r) 452)
    (= (luminance r) 373)
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
