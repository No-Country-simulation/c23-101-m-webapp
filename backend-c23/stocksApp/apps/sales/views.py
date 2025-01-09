from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    @action(detail=False, methods=['get'])
    def total_sales(self, request):
        total_sales = self.queryset.aggregate(models.Sum('total'))['total__sum'] or 0.00
        return Response({'total_sales': total_sales})

class ProfitReportViewSet(viewsets.ViewSet):
    def list(self, request):
        reports = ProfitReport.objects.all()
        for report in reports:
            report.update_report()
        serializer = ProfitReportSerializer(reports, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def update(self, request, pk=None):
        report = ProfitReport.objects.get(pk=pk)
        report.update_report()
        serializer = ProfitReportSerializer(report)
        return Response(serializer.data)