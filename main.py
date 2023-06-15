import json
import random
from fastapi import FastAPI
import asyncio
from starlette.responses import StreamingResponse

app = FastAPI(debug=True)

@app.get('/stream', response_class=StreamingResponse)
async def stream_data():
    async def generate_healthcare_data():
        actions = ['run', 'sit', 'walk']
        
        action = random.choice(actions)
        record = {}
        patient_type = f's1_{action}'
        record['patienttype'] = patient_type
        values = patient_type.split('_')[1:]
        record['values'] = ''.join(values)

        if action == 'run':
            record['bp_sys_start'] = random.randint(100, 165)
            record['bp_sys_end'] = random.randint(100, 165)
            record['bp_dia_start'] = random.randint(65, 93)
            record['bp_dia_end'] = random.randint(65, 93)
            record['hr_1_start'] = random.randint(80, 115)
            record['hr_1_end'] = random.randint(80, 120)
            record['hr_2_start'] = random.randint(80, 120)
            record['hr_2_end'] = random.randint(80, 120)
            record['spo2_start'] = random.randint(90, 120)
            record['spo2_end'] = random.randint(90, 120)
        elif action == 'sit':
            record['bp_sys_start'] = random.randint(80, 100)
            record['bp_sys_end'] = random.randint(80, 100)
            record['bp_dia_start'] = random.randint(55, 60)
            record['bp_dia_end'] = random.randint(55, 60)
            record['hr_1_start'] = random.randint(60, 80)
            record['hr_1_end'] = random.randint(60, 80)
            record['hr_2_start'] = random.randint(60, 80)
            record['hr_2_end'] = random.randint(60, 80)
            record['spo2_start'] = random.randint(80, 90)
            record['spo2_end'] = random.randint(80, 90)
        elif action == 'walk':
            record['bp_sys_start'] = random.randint(90, 100)
            record['bp_sys_end'] = random.randint(90, 100)
            record['bp_dia_start'] = random.randint(55, 70)
            record['bp_dia_end'] = random.randint(55, 70)
            record['hr_1_start'] = random.randint(70, 90)
            record['hr_1_end'] = random.randint(70, 90)
            record['hr_2_start'] = random.randint(70, 90)
            record['hr_2_end'] = random.randint(70, 90)
            record['spo2_start'] = random.randint(85, 95)
            record['spo2_end'] = random.randint(85, 95)

        record['Height'] = random.randint(150, 200)
        record['Weight'] = random.randint(40, 150)
        record['Age'] = random.randint(18, 98)

        yield json.dumps(record) + '\n'

    async def stream_generator():
        async for data in generate_healthcare_data():
            yield data

    return StreamingResponse(stream_generator())
