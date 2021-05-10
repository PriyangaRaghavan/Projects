(define (problem p1)
(:domain test)
(:objects 
   r - room h - heater w - window l - light p - occupancy)
(:init 
    (open w)
    (presence p)
    (on-light l)

    (= (temp r) 28)
    (= (air-quality r) 340)
    (= (luminance r) 502)
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
