from Events.ExtraordinaryEvent import ExtraordinaryEvent
from Events.ArUcoEvent import ArUcoEvent
from Events.InfrastructureEvent import InfrastructureEvent
from Events.WorkerEvent import WorkerEvent
import RandomEvent

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image, Spacer


class PDFator:
    # Function to create a PDF with a table and images
    def generate_table_sizes(self, data, width, is_first_numbered=False, jury_last=True):
        cols = len(data[0])
        jury_w = 30.0
        index_w = 15.0
        widths = []

        if jury_last:
            width = width - jury_w
            cols -= 1

        
        if is_first_numbered:
            width = width - index_w
            cols -= 1
        
        widths = [width / cols] * cols

        if is_first_numbered:
            widths.insert(0, index_w)

        if jury_last:
            widths.append(jury_w)

        return Table(data, colWidths=widths)

    def get_table_style(self):
        return TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    def add_element(self, table, text, elements):
        elements.append(Spacer(1, 10))
        elements.append(Paragraph(
            text, getSampleStyleSheet()['Normal']))
        elements.append(Spacer(1, 10))
        elements.append(table)
        return elements

    def create_pdf(self):
        # Create a PDF document
        doc = SimpleDocTemplate(self.output_file, title="TOP SECRET", author="CIA", pagesize=A4, leftMargin=10,
                                rightMargin=10, topMargin=10, bottomMargin=10)

        width, height = A4
        width = width - 30.0

        # Create a table with the provided data and set colWidths to page width
        table1 = self.generate_table_sizes(self.table_data1, width)
        table2 = self.generate_table_sizes(self.table_data2, width)
        table3 = self.generate_table_sizes(self.table_data3, width, is_first_numbered=True)
        table4 = self.generate_table_sizes(self.table_data4, width, is_first_numbered=True)
        table5 = self.generate_table_sizes(self.table_data5, width, is_first_numbered=True)
        table6 = self.generate_table_sizes(self.table_data6, width, is_first_numbered=True)
        table8 = Table(self.table_data8, colWidths=[(0.8*width), (width*0.2)])


        # Add style to the table
        style8 = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)])
        

        style1 = self.get_table_style()
        style2 = self.get_table_style()
        style3 = self.get_table_style()
        style4 = self.get_table_style()
        style5 = self.get_table_style()
        style6 = self.get_table_style()
        # style8 = get_table_style()

        table1.setStyle(style1)
        table2.setStyle(style2)

        # Create a list to hold the elements in the PDF
        elements = []

        # pdf heading
        elements.append(Paragraph('Raport z konkurencji inspeckcja',
                        getSampleStyleSheet()['Heading1']))
        list_text = '''
        <seq/>. Podstawowe informacje o wykonanej misji;
        <seq/>. Dodatkowe informacje o wykonanej misji;
        <seq/>. Lista pracownikow znajdujacych sie na terenie;
        <seq/>. Zmiany w infrastrukturze;
        <seq/>. Sytuacje nadzwyczajne;
        <seq/>. Kody ArUco;
        <seq/>. Mapa infrastruktury;
        <seq/>. Informacje koncowe
        '''
        elements.append(Paragraph('Spis Tresci', getSampleStyleSheet()['Normal']))
        for line in list_text.split(';'):
            elements.append(Paragraph(line.strip(), getSampleStyleSheet()['Normal']))

        elements = self.add_element(table1, '1. Podstawowe informacje o wykonanej misji', elements)
        elements = self.add_element(table2, '1. Dodatkowe informacje o wykonanej misji', elements)


        # Merge cells in the first row of table1
        style3.add('SPAN', (0, 0), (5, 0))
        table3.setStyle(style3)
        elements = self.add_element(table3, '3. Lista pracownikow znajdujacych sie na terenie zalkadu (Max. liczba pracownikow = 6)', elements)


        # Merge cells in the first row of table1
        style4.add('SPAN', (0, 0), (4, 0))
        table4.setStyle(style4)
        elements = self.add_element(table4, '4. Zmiany w infrastrukturze w stosunku do lotu “Zero”', elements)


        # Merge cells in the first row of table1
        style5.add('SPAN', (0, 0), (5, 0))
        table5.setStyle(style5)
        elements = self.add_element(table5, '5. sytuacje nadzwyczajne', elements)   

        # Merge cells in the first row of table1
        style6.add('SPAN', (0, 0), (5, 0))
        table6.setStyle(style6)
        elements = self.add_element(table6, '6. Kody ArUco', elements)


        elements.append(Spacer(1, 10))
        elements.append(Paragraph(
            '7. Mapa Infrastruktury', getSampleStyleSheet()['Normal']))
        elements.append(Spacer(1, 10))
        
        img = Image(self.map_path, width=200, height=150)
        elements.append(img)
        elements.append(Spacer(1, 10))


        table8.setStyle(style8)
        elements = self.add_element(table8, '8. Informacje koncowe', elements)

        # Build the PDF document
        doc.build(elements)
        print(f"PDF generated successfully. File saved at: {self.output_file}")
    
    def add_worker_event(self, worker_event: WorkerEvent):
        to_append = [self.worker_event_count]
        self.worker_event_count += 1
        to_append.extend(worker_event.get_worker_event())
        to_append.extend(' ')
        self.table_data3.append(to_append)

    def add_infrastructure_event(self, infrastructure_event: InfrastructureEvent):
        to_append = [self.infrastructure_event_count]
        self.infrastructure_event_count += 1
        to_append.extend(infrastructure_event.get_infrastructure_event())
        to_append.extend(' ')
        self.table_data4.append(to_append)
    
    def add_extraordinary_event(self, extraordinary_event: ExtraordinaryEvent):
        to_append = [self.extraordinary_event_count]
        self.extraordinary_event_count += 1
        to_append.extend(extraordinary_event.get_extraordinary_event())
        to_append.extend(' ')
        self.table_data5.append(to_append)
    
    def add_aruco_event(self, aruco_event: ArUcoEvent):
        to_append = [self.aruco_event_count]
        self.aruco_event_count += 1
        to_append.extend(aruco_event.get_aruco_event())
        to_append.extend(' ')
        self.table_data6.append(to_append)

    def __init__(self):
        
        self.worker_event_count = 1
        self.infrastructure_event_count = 1
        self.extraordinary_event_count = 1
        self.aruco_event_count = 1


        self.table_data1 = [
            ['', 'Zespol', 'Jury'],
            ['Nazwa / Email', '[Nazwa zespolu / email]', '+/-'],
            ['Nazwisko pilota / nr komorki ', '[Imie Nazwisko, nr komorki]', '+/-'],
            ['Data i godzina rozpoczecia misji ', '[DD/MM/RRRR, GG:MM:SS]', '+/-'],
            ['Nr misji', '[ZERO] [01] [02] [03] ', '+/-'],
            ['Czas trwania lotu ', '[MM:SS]', '+/-'],
            ['Stan baterii przed wykonaniem lotu', '[X% / XX V]', '+/-']
        ]

        self.table_data2 = [
            ['', 'Zespol', 'Jury'],
            ['Index KP', '[X Kp]', '+/-'],
            ['Stan batteri po zakonczeniu misji', '[X% / XX V]', '+/-'],
        ]

        self.table_data3 = [
            ['Zespol',                       '',    '',                                         '',                           '',        '', 'Jury'],
            ['#'     , 'Pracownik\nJest/Nie ma', 'BHP', 'Lokalizacja\n(Jesli wykryto\npracownika)', 'Zmiana wzgledem\nlotu ZERO', 'Zdjecje', ' ']
        ]

        self.table_data4 = [
            [ 'Zespol',           '',              '',           '',        '', 'Jury'],
            ['#'      , 'Kategoraia', 'Czas Wykrycia', 'Lokaizacja', 'Zdjecie', ' '],
            
        ]

        self.table_data5 = [
            [ 'Zespol',     '',    '',           '',        '',              '', 'Jury'],
            ['#', 'Zdarzenie', 'Czas', 'Lokaizacja', 'Zdjecie', 'Powiadomienie', ' ']
        ]

        self.table_data6 = [
            [ 'Zespol',    '',            '',                                       '',                                       '',        '', 'Jury'],
            ['#', 'Zawartosc', 'Lokalizacja', 'zmiana lokalizacj\nwzgledem\nlotu ZERO', 'zmiana zawartosci\nwzgledem\nlotu ZERO', 'Zdjecie', ' ']
        ]

        self.table_data8 = [
            [ 'Uzupelnia Komisja Sedziowska', 'Pkt'],
            ['Lot ZERO z poprawnym przygotowanym raportem poczatkowym',  ' '],
            ['Automatyczny start, lot i ladowanie',  ' '],
            ['Poprawne wykrycie i raportowanie zmiany w infrastrukturze stalej (zmiany statyczne)',  ' '],
            ['Poprawne wykrycie i raportowanie o pracownikach',  ' '],
            ['Poprawne wykrycie zdarzenia nadzwyczajnego',  ' '],
            ['Wykrycie i odczytanie kodów ArUCo',  ' '],
            ['Najkrótszy czas wykonania calej misji (lot + raport)',  ' '],
            ['Premia za wyslanie raportu jeszcze w trakcie lotu lub jednoczesnie wraz z ladowaniem',  ' '],
            ['Punkty karne',  ' '],
            ['Suma punktów',  ' ']
        ]

        # Example image paths
        self.map_path = './img/map.jpg'

        # Output file path
        self.output_file = 'TOP_SECRET.pdf'




if __name__ == '__main__':
    pdfator = PDFator()
    worker_events = RandomEvent.worker(5)
    infrastructure_events = RandomEvent.infrastructure(5)
    extraordinary_events = RandomEvent.extraordinary(5)
    aruco_events = RandomEvent.aruco(5)

    for worker_event in worker_events:
        pdfator.add_worker_event(worker_event)
    
    for infrastructure_event in infrastructure_events:
        pdfator.add_infrastructure_event(infrastructure_event)
    
    for extraordinary_event in extraordinary_events:
        pdfator.add_extraordinary_event(extraordinary_event)
    
    for aruco_event in aruco_events:
        pdfator.add_aruco_event(aruco_event)
    
    pdfator.create_pdf()