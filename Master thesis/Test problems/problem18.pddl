(define (problem p18)
(:domain test)
(:objects 
   r - room h - heater w - window l - light p - occupancy)
(:init 
    (presence p)
    (on_heater h)
    (= (temp r) 24.9)
    (= (air-quality r) 653)
    (= (luminance r) 400)
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
