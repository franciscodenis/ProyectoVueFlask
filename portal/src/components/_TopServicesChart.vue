<template>
    <div>
      <h2>Ranking de Servicios Más Solicitados</h2>
      <div ref="chartContainer" class="chart-container">
            <svg ref="chart"></svg>
        </div>
    </div>
</template>

<script>
import * as d3 from 'd3';
import { apiService } from '../services/api';

export default {
data() {
    return {
    topServices: [],
    };
},
mounted() {
    this.fetchTopServices();
},
methods: {
    fetchTopServices() {
    apiService.get('/api/data/top-services')
        .then(response => {
        this.topServices = response.data;
        this.createChart();
        })
        .catch(error => {
        console.error('Error al cargar datos', error);
        });
    },
    createChart() {
    const width = this.$refs.chartContainer.clientWidth;
    const height = 300;
    const margin = { top: 20, right: 20, bottom: 30, left: 40 };

    // Define una escala de colores ordinal
    const colorScale = d3.scaleOrdinal(d3.schemeCategory10);

    const svg = d3.select(this.$refs.chart)
        .attr('width', width)
        .attr('height', height);

    const xScale = d3.scaleBand()
        .domain(this.topServices.map(service => service.service))
        .range([margin.left, width - margin.right])
        .padding(0.1);

    const yScale = d3.scaleLinear()
        .domain([0, d3.max(this.topServices, d => d.count)])
        .range([height - margin.bottom, margin.top]);

    const bars = svg.selectAll('rect')
        .data(this.topServices)
        .enter()
        .append('rect')
        .attr('x', d => xScale(d.service))
        .attr('y', d => yScale(d.count))
        .attr('width', xScale.bandwidth())
        .attr('height', d => height - margin.bottom - yScale(d.count))
        .attr('fill', (d, i) => colorScale(i)); // Asigna colores en función del índice

    svg.append('g')
        .attr('transform', `translate(0,${height - margin.bottom})`)
        .call(d3.axisBottom(xScale));

    svg.append('g')
        .attr('transform', `translate(${margin.left},0)`)
        .call(d3.axisLeft(yScale));

    // Etiquetas
    svg.selectAll('.label')
        .data(this.topServices)
        .enter()
        .append('text')
        .text(d => d.count)
        .attr('x', d => xScale(d.service) + xScale.bandwidth() / 2)
        .attr('y', d => yScale(d.count) - 5)
        .attr('text-anchor', 'middle')
        .attr('class', 'label');
    },
    },
};
</script>

<style scoped>
/* Estilos específicos del componente si es necesario */
rect {
    transition: fill 0.3s ease;
}

rect:hover {
    fill: darkblue;
}
</style>