<template>
    <div>
        <h2>Top 10 de las Instituciones con mejor tiempo de resolución</h2>
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
    topInstitutions: [],
    };
},
mounted() {
    this.fetchTopInstitutions();
},
methods: {
    fetchTopInstitutions() {
    apiService.get('/api/data/top-institutions')
        .then(response => {
        this.topInstitutions = response.data;
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
        .domain(this.topInstitutions.map(institution => institution.institution))
        .range([margin.left, width - margin.right])
        .padding(0.1);

    const yScale = d3.scaleLinear()
        .domain([0, d3.max(this.topInstitutions, d => d.avg_resolution_time)])
        .range([height - margin.bottom, margin.top]);

    const bars = svg.selectAll('rect')
        .data(this.topInstitutions)
        .enter()
        .append('rect')
        .attr('x', d => xScale(d.institution))
        .attr('y', d => yScale(d.avg_resolution_time))
        .attr('width', xScale.bandwidth())
        .attr('height', d => height - margin.bottom - yScale(d.avg_resolution_time))
        .attr('fill', (d, i) => colorScale(i)); // Asigna colores en función del índice

    svg.append('g')
        .attr('transform', `translate(0,${height - margin.bottom})`)
        .call(d3.axisBottom(xScale));

    svg.append('g')
        .attr('transform', `translate(${margin.left},0)`)
        .call(d3.axisLeft(yScale));

    // Etiquetas
    svg.selectAll('.label')
        .data(this.topInstitutions)
        .enter()
        .append('text')
        .text(d => `${d.avg_resolution_time.toFixed(2)} segundos`)
        .attr('x', d => xScale(d.institution) + xScale.bandwidth() / 2)
        .attr('y', d => yScale(d.avg_resolution_time) - 5)
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