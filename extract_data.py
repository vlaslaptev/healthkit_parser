import psycopg2
import xml.etree.ElementTree as ET

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="***",
    password="***"
)
cursor = conn.cursor()

# Parse the XML file
tree = ET.parse('/tmp/apple_health.xml')
root = tree.getroot()

# Insert records into the public.apple_export_record table
for record in root.findall('Record'):
    cursor.execute("""
        INSERT INTO public.apple_export_record (
            record_type, source_name, source_version, unit,
            creation_date, start_date, end_date, record_value
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        record.attrib.get('type'), record.attrib.get('sourceName'), record.attrib.get('sourceVersion'),
        record.attrib.get('unit'), record.attrib.get('creationDate'), record.attrib.get('startDate'),
        record.attrib.get('endDate'), record.attrib.get('value')
    ))

# Insert records into the public.apple_export_workout table
for workout in root.findall('Workout'):
    cursor.execute("""
        INSERT INTO public.apple_export_workout (
            workout_activity_type, duration, duration_unit,
            source_name, source_version, device,
            creation_date, start_date, end_date
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        workout.attrib.get('workoutActivityType'), workout.attrib.get('duration'), workout.attrib.get('durationUnit'),
        workout.attrib.get('sourceName'), workout.attrib.get('sourceVersion'), workout.attrib.get('device'),
        workout.attrib.get('creationDate'), workout.attrib.get('startDate'), workout.attrib.get('endDate')
    ))

# Insert records into the public.apple_export_activity_summary table
for summary in root.findall('ActivitySummary'):
    cursor.execute("""
        INSERT INTO public.apple_export_activity_summary (
            date_components, active_energy_burned, active_energy_burned_goal, active_energy_burned_unit,
            apple_move_time, apple_move_time_goal, apple_exercise_time,
            apple_exercise_time_goal, apple_stand_hours, apple_stand_hours_goal
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        summary.attrib.get('dateComponents'), summary.attrib.get('activeEnergyBurned'), summary.attrib.get('activeEnergyBurnedGoal'),
        summary.attrib.get('activeEnergyBurnedUnit'), summary.attrib.get('appleMoveTime'), summary.attrib.get('appleMoveTimeGoal'),
        summary.attrib.get('appleExerciseTime'), summary.attrib.get('appleExerciseTimeGoal'),
        summary.attrib.get('appleStandHours'), summary.attrib.get('appleStandHoursGoal')
    ))

# Commit the transaction and close the connection
conn.commit()
cursor.close()
conn.close()
