import React, { useState, useEffect } from 'react';
import { Play, Pause, RotateCcw, SkipForward } from 'lucide-react';

const TreeBFSVisualization = () => {
  // Tree structure matching your Python code
  const treeData = {
    value: 5,
    left: {
      value: 12,
      left: {
        value: 7,
        left: { value: 17, left: null, right: null },
        right: { value: 23, left: null, right: null }
      },
      right: {
        value: 14,
        left: { value: 27, left: null, right: null },
        right: { value: 3, left: null, right: null }
      }
    },
    right: {
      value: 13,
      left: null,
      right: {
        value: 2,
        left: { value: 8, left: null, right: null },
        right: { value: 11, left: null, right: null }
      }
    }
  };

  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [steps, setSteps] = useState([]);

  // Generate BFS steps
  useEffect(() => {
    const generateSteps = () => {
      const stepsArray = [];
      const queue = [{ node: treeData, level: 0 }];
      const visited = new Set();

      // Initial state
      stepsArray.push({
        queue: [{ value: treeData.value, level: 0 }],
        current: null,
        visited: [],
        result: [],
        level: 0,
        description: 'Initialize queue with root node'
      });

      let result = [];

      while (queue.length > 0) {
        const queueSnapshot = queue.map(q => ({ value: q.node.value, level: q.level }));
        const { node, level } = queue.shift();

        visited.add(node.value);

        if (!result[level]) {
          result[level] = [];
        }
        result[level].push(node.value);

        // Step: Processing current node
        stepsArray.push({
          queue: queueSnapshot.slice(1),
          current: { value: node.value, level },
          visited: Array.from(visited),
          result: JSON.parse(JSON.stringify(result)),
          level,
          description: `Dequeue and process node ${node.value} (Level ${level})`
        });

        // Add children to queue
        const childrenAdded = [];
        if (node.left) {
          queue.push({ node: node.left, level: level + 1 });
          childrenAdded.push(node.left.value);
        }
        if (node.right) {
          queue.push({ node: node.right, level: level + 1 });
          childrenAdded.push(node.right.value);
        }

        if (childrenAdded.length > 0) {
          stepsArray.push({
            queue: queue.map(q => ({ value: q.node.value, level: q.level })),
            current: { value: node.value, level },
            visited: Array.from(visited),
            result: JSON.parse(JSON.stringify(result)),
            level,
            description: `Add children [${childrenAdded.join(', ')}] to queue`
          });
        }
      }

      // Final state
      stepsArray.push({
        queue: [],
        current: null,
        visited: Array.from(visited),
        result,
        level: -1,
        description: 'BFS traversal complete!'
      });

      setSteps(stepsArray);
    };

    generateSteps();
  }, []);

  // Auto-play functionality
  useEffect(() => {
    let interval;
    if (isPlaying && currentStep < steps.length - 1) {
      interval = setInterval(() => {
        setCurrentStep(prev => {
          if (prev >= steps.length - 1) {
            setIsPlaying(false);
            return prev;
          }
          return prev + 1;
        });
      }, 1500);
    }
    return () => clearInterval(interval);
  }, [isPlaying, currentStep, steps.length]);

  const currentStepData = steps[currentStep] || {
    queue: [],
    current: null,
    visited: [],
    result: [],
    level: 0,
    description: ''
  };

  // Tree node component
  const TreeNode = ({ node, level = 0, x = 400, y = 50 }) => {
    if (!node) return null;

    const isVisited = currentStepData.visited.includes(node.value);
    const isCurrent = currentStepData.current?.value === node.value;
    const inQueue = currentStepData.queue.some(q => q.value === node.value);

    const horizontalSpacing = 400 / Math.pow(2, level + 1);
    const verticalSpacing = 80;

    return (
      <>
        {/* Lines to children */}
        {node.left && (
          <line
            x1={x}
            y1={y}
            x2={x - horizontalSpacing}
            y2={y + verticalSpacing}
            stroke="#94a3b8"
            strokeWidth="2"
          />
        )}
        {node.right && (
          <line
            x1={x}
            y1={y}
            x2={x + horizontalSpacing}
            y2={y + verticalSpacing}
            stroke="#94a3b8"
            strokeWidth="2"
          />
        )}

        {/* Node circle */}
        <circle
          cx={x}
          cy={y}
          r="25"
          fill={isCurrent ? '#ef4444' : isVisited ? '#10b981' : inQueue ? '#3b82f6' : '#e2e8f0'}
          stroke={isCurrent ? '#dc2626' : isVisited ? '#059669' : inQueue ? '#2563eb' : '#cbd5e1'}
          strokeWidth="3"
        />
        <text
          x={x}
          y={y}
          textAnchor="middle"
          dominantBaseline="middle"
          fill={isCurrent || isVisited || inQueue ? 'white' : '#1e293b'}
          fontSize="16"
          fontWeight="bold"
        >
          {node.value}
        </text>

        {/* Recursively render children */}
        {node.left && (
          <TreeNode
            node={node.left}
            level={level + 1}
            x={x - horizontalSpacing}
            y={y + verticalSpacing}
          />
        )}
        {node.right && (
          <TreeNode
            node={node.right}
            level={level + 1}
            x={x + horizontalSpacing}
            y={y + verticalSpacing}
          />
        )}
      </>
    );
  };

  return (
    <div className="w-full max-w-6xl mx-auto p-6 bg-gray-50 rounded-lg">
      <h1 className="text-3xl font-bold text-center mb-6 text-gray-800">
        BFS Tree Traversal Visualization
      </h1>

      {/* Tree Visualization */}
      <div className="bg-white rounded-lg shadow-lg p-4 mb-6">
        <svg width="800" height="400" className="mx-auto">
          <TreeNode node={treeData} />
        </svg>
      </div>

      {/* Queue Visualization */}
      <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
        <h2 className="text-xl font-semibold mb-4 text-gray-700">
          Queue State (FIFO - First In, First Out)
        </h2>
        <div className="flex items-center gap-2 min-h-[80px]">
          <div className="text-sm font-semibold text-gray-600">Front →</div>
          {currentStepData.queue.length === 0 ? (
            <div className="flex-1 text-center text-gray-400 italic">Queue is empty</div>
          ) : (
            currentStepData.queue.map((item, idx) => (
              <div
                key={idx}
                className="flex flex-col items-center bg-blue-500 text-white rounded-lg p-4 min-w-[80px] shadow-md"
              >
                <div className="text-2xl font-bold">{item.value}</div>
                <div className="text-xs mt-1">Level {item.level}</div>
              </div>
            ))
          )}
          <div className="text-sm font-semibold text-gray-600">← Back</div>
        </div>
      </div>

      {/* Current Processing */}
      <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
        <h2 className="text-xl font-semibold mb-4 text-gray-700">Currently Processing</h2>
        {currentStepData.current ? (
          <div className="flex items-center gap-4">
            <div className="bg-red-500 text-white rounded-lg p-6 min-w-[100px] text-center shadow-md">
              <div className="text-3xl font-bold">{currentStepData.current.value}</div>
              <div className="text-sm mt-2">Level {currentStepData.current.level}</div>
            </div>
            <div className="text-gray-600">
              <p className="font-semibold">{currentStepData.description}</p>
            </div>
          </div>
        ) : (
          <div className="text-gray-400 italic">{currentStepData.description}</div>
        )}
      </div>

      {/* Result by Level */}
      <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
        <h2 className="text-xl font-semibold mb-4 text-gray-700">Result (Level Order)</h2>
        {currentStepData.result.length === 0 ? (
          <div className="text-gray-400 italic">No nodes processed yet</div>
        ) : (
          <div className="space-y-3">
            {currentStepData.result.map((level, idx) => (
              <div key={idx} className="flex items-center gap-3">
                <div className="font-semibold text-gray-600 min-w-[80px]">Level {idx}:</div>
                <div className="flex gap-2">
                  {level.map((value, vidx) => (
                    <div
                      key={vidx}
                      className="bg-green-500 text-white rounded-lg px-4 py-2 font-bold shadow"
                    >
                      {value}
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Controls */}
      <div className="bg-white rounded-lg shadow-lg p-6">
        <div className="flex items-center justify-center gap-4">
          <button
            onClick={() => setCurrentStep(0)}
            className="px-4 py-2 bg-gray-600 text-white rounded-lg hover:bg-gray-700 transition flex items-center gap-2"
          >
            <RotateCcw size={20} />
            Reset
          </button>
          <button
            onClick={() => setCurrentStep(prev => Math.max(0, prev - 1))}
            disabled={currentStep === 0}
            className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition disabled:bg-gray-300 disabled:cursor-not-allowed"
          >
            Previous
          </button>
          <button
            onClick={() => setIsPlaying(!isPlaying)}
            className="px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition flex items-center gap-2"
          >
            {isPlaying ? <Pause size={20} /> : <Play size={20} />}
            {isPlaying ? 'Pause' : 'Play'}
          </button>
          <button
            onClick={() => setCurrentStep(prev => Math.min(steps.length - 1, prev + 1))}
            disabled={currentStep === steps.length - 1}
            className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition disabled:bg-gray-300 disabled:cursor-not-allowed flex items-center gap-2"
          >
            Next
            <SkipForward size={20} />
          </button>
        </div>
        <div className="mt-4 text-center text-gray-600">
          Step {currentStep + 1} of {steps.length}
        </div>
      </div>

      {/* Legend */}
      <div className="bg-white rounded-lg shadow-lg p-6 mt-6">
        <h2 className="text-xl font-semibold mb-4 text-gray-700">Legend</h2>
        <div className="flex flex-wrap gap-6">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-full bg-red-500"></div>
            <span>Currently Processing</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-full bg-blue-500"></div>
            <span>In Queue</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-full bg-green-500"></div>
            <span>Visited</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-full bg-gray-300"></div>
            <span>Not Visited</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TreeBFSVisualization;
