(define (domain test)
  (:requirements :strips :typing :fluents  :negative-preconditions :adl :disjunctive-preconditions)
  (:types 
   room heater window light occupancy- object)

  (:predicates
           (on_heater ?h - heater)
           (open ?w - window)
           (on-light ?l - light)
           (presence ?p - occupancy)
  )

   (:functions
       (temp ?r - room)
       (air-quality ?r - room)
       (luminance ?r - room)
       (temp-threshold-high)
       (temp-threshold-low)
       (air-quality-threshold-high)
       (air-quality-threshold-low)
       (luminance-threshold)
   )

  
   (:action switch_off_heater
        :parameters (?h - heater ?r - room)
        :precondition (or (on_heater ?h) (>(temp ?r) (temp-threshold-high)))
        :effect (and(not(on_heater ?h))(decrease (temp ?r) (- (temp ?r) (temp-threshold-high) )))
   )

   (:action switch_on_heater
            :parameters(?h - heater ?r - room)
            :precondition(and (not(on_heater ?h)) (<(temp ?r) (temp-threshold-low)))
            :effect(and(on_heater ?h) (increase (temp ?r) (-(temp-threshold-low) (temp ?r))) )
   )

   (:action open_window
            :parameters(?w - window ?r - room)
            :precondition(and (not(open ?w)) (>(air-quality ?r)(air-quality-threshold-high)))
            :effect (and (open ?w) (decrease (air-quality ?r) (- (air-quality ?r) (air-quality-threshold-high))) )
   )

   (:action close_window
            :parameters(?w - window ?r - room)
            :precondition(and (open ?w) (<(air-quality ?r)(air-quality-threshold-low)))
            :effect(and (not(open ?w)) (increase (air-quality ?r) (- (air-quality-threshold-low) (air-quality ?r) )))
   )

   (:action switch_on_light
            :parameters(?l - light ?r - room ?p - occupancy)
            :precondition(and (not(on-light ?l)) (presence ?p) (<(luminance ?r) (luminance-threshold)))
            :effect (and (on-light ?l) (increase (luminance ?r) 300))
   )

   (:action switch_off_light
            :parameters(?l - light ?r - room ?p - occupancy)
            :precondition(and (on-light ?l) (not(presence ?p)))
            :effect (and (not(on-light ?l)))
   )
 
  
   
)



   
   
