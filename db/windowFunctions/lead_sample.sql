SELECT
    tf.ticket_no,
    f.departure_airport,
    f.arrival_airport,
    f.scheduled_arrival,
    lead(f.scheduled_departure) OVER w AS next_departure,
    lead(f.scheduled_departure) OVER w - f.scheduled_arrival AS gap
from
    bookings b
    JOIN tickets t ON t.book_ref = b.book_ref
    JOIN ticket_flights tf ON tf.ticket_no = t.ticket_no
    JOIN flights f ON tf.flight_id = f.flight_id
where
    b.book_date = bookings.now()::date - INTERVAL '7 day'
window w AS (
    PARTITION BY tf.ticket_no
    ORDER BY f.scheduled_departure
    );