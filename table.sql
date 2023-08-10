create table public.apple_export_record
(
    id             bigserial primary key,
    record_type    text,
    source_name    text,
    source_version text,
    unit           text,
    creation_date  text,
    start_date     text,
    end_date       text,
    record_value   text
);

create table public.apple_export_workout
(
    id                    bigserial primary key,
    workout_activity_type text,
    duration              text,
    duration_unit         text,
    source_name           text,
    source_version        text,
    device                text,
    creation_date         text,
    start_date            text,
    end_date              text
);

create table public.apple_export_activity_summary
(
    id                        bigserial primary key,
    date_components           text,
    active_energy_burned      text,
    active_energy_burned_goal text,
    active_energy_burned_unit text,
    apple_move_time           text,
    apple_move_time_goal      text,
    apple_exercise_time       text,
    apple_exercise_time_goal  text,
    apple_stand_hours         text,
    apple_stand_hours_goal    text
);
