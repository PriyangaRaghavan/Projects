(define (problem p13)
(:domain test)
(:objects 
   r - room h - heater w - window l - light p - occupancy)
(:init 
    (on_heater h)
    (= (temp r) 26.1)
    (= (air-quality r) 723)
    (= (luminance r) 620)
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
