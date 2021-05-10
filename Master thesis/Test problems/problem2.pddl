(define (problem p2)
(:domain test)
(:objects 
   r - room h - heater w - window l - light p - occupancy)
(:init 
    (open w)
    (on_heater h)
    (presence p)

    (= (temp r) 23.2)
    (= (air-quality r) 360)
    (= (luminance r) 390)
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
