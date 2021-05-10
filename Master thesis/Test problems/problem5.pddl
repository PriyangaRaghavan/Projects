(define (problem p5)
(:domain test)
(:objects 
   r - room h - heater w - window l - light p - occupancy)
(:init 
    (on-light l)
    (open w)

    (= (temp r) 20.6)
    (= (air-quality r) 725)
    (= (luminance r) 420)
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
