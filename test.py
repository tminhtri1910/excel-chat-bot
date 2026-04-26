import pandas as pd

df = pd.read_excel("uploads/Công khai DS công chức thuế hỗ trợ NNT (final).xls", usecols='A:H', skiprows=8)

print(df[df['TÊN DOANH NGHIỆP/ HỘ KINH DOANH/CÁ NHÂN KINH DOANH'].isin(['HỘ KINH DOANH NHÀ THUỐC NGHĨA HƯNG 1', 'HỘ KINH DOANH SELF NAIL & CARE'])]['MÃ SỐ THUẾ DOANH NGHIỆP/ HỘ KINH DOANH/CÁ NHÂN KINH DOANH'].tolist())

# print(df['PHÒNG/TỔ ĐANG CÔNG TÁC'].unique())
# print(df[df['PHÒNG/TỔ ĐANG CÔNG TÁC'] == 'Tổ Quản lý, hỗ trợ hộ cá nhân, hộ kinh doanh số 1'].shape[0])
