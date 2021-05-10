(define (problem p21)
(:domain test)
(:objects 
   r - room h - heater w - window l - light p - occupancy)
(:init 
    



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
