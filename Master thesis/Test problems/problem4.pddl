(define (problem p4)
(:domain test)
(:objects 
   r - room h - heater w - window l - light p - occupancy)
(:init 
    (open w)
    (on_heater h)
    (presence p)
    
    (= (temp r) 22.2)
    (= (air-quality r) 425)
    (= (luminance r) 389)
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
