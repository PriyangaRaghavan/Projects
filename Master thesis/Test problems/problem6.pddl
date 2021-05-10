(define (problem p6)
(:domain test)
(:objects 
   r - room h - heater w - window l - light p - occupancy)
(:init 
   (on-light l)   
   (presence p)
   (open w)
   (= (temp r) 20.6)
   (= (air-quality r) 421)
   (= (luminance r) 412)    

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
